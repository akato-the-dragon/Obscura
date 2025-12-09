from typing import Optional
from PySide6.QtCore import QObject, Signal
from fastapi import FastAPI, HTTPException
from core.data_base import password_database
from fastapi.middleware.cors import CORSMiddleware
import datetime
import asyncio
import threading
from uvicorn import Config, Server


class ExtensionService(QObject):
    server_started = Signal()
    server_stoped = Signal()
    password_recieved = Signal()
    password_sended = Signal()

    def __init__(self, host: str = "127.0.0.1", port: int = 8000, parent: Optional[QObject] = None) -> None:
        super().__init__(parent)

        self._app = FastAPI()
        self._host = host
        self._port = port

        self._running = False
        self._extension_responce_timeout = 30
        self._last_extension_responce = None
        self._server_thread = None
        self._server = None
        self._loop = None

        self.__backend()
    
    def __backend(self) -> None:
        self._app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )

        @self._app.post("/extension/ping")
        async def ping_extension():
            self._last_extension_responce = datetime.datetime.now()
            return {"connected": True, "timestamp": self._last_extension_responce.isoformat()}

        @self._app.get("/credentials/{site_url}")
        async def get_credentials(site_url: str):
            password_list = password_database.get_password_list()

            for password_item in password_list:
                if (password_item[1] == site_url or password_item[1].endswith(site_url) or site_url.endswith(password_item[1])):
                    # ОШИБКА: здесь должно быть password_item[0], а не password[0]
                    id, url, login, password = password_database.get_password_item(password_item[0])

                    return {
                        "login": login,
                        "password": password
                    }

            raise HTTPException(status_code=404, detail="No credentials for this domain")

        @self._app.post("/credentials")
        async def save_credentials(data: dict):
            site_url = data.get("domain")
            login = data.get("login")
            password = data.get("password")
            
            password_database.add_password(site_url, login, password)

    def is_extension_online(self) -> bool:
        if isinstance(self._last_extension_responce, datetime.datetime):
            return (datetime.datetime.now() - self._last_extension_responce).seconds < self._extension_responce_timeout
        return False

    def is_service_online(self) -> bool:
        return self._running

    def _run_server(self):
        try:
            config = Config(app=self._app, host=self._host, port=self._port, loop="asyncio")
            self._server = Server(config=config)
            
            self._loop = asyncio.new_event_loop()
            asyncio.set_event_loop(self._loop)
            
            self._loop.run_until_complete(self._server.serve())
        except Exception as e:
            print(f"Server error: {e}")
        finally:
            if self._loop:
                self._loop.close()

    def start_service(self) -> None:
        if self._running:
            return
            
        self._server_thread = threading.Thread(target=self._run_server, daemon=True)
        self._server_thread.start()
        
        self._running = True
        self.server_started.emit()

    def stop_service(self) -> None:
        if not self._running:
            return
            
        if self._server:
            self._server.should_exit = True
            
        if self._server_thread and self._server_thread.is_alive():
            self._server_thread.join(timeout=2.0)
            
        self._server = None
        self._server_thread = None
        self._loop = None
        
        self._running = False
        self.server_stoped.emit()
