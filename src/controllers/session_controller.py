from datetime import datetime
from typing import Dict, List, Optional


class SessionManager:
    def __init__(self):
        self._sessions: Dict[str, dict] = {}

    def start_session(self, name: str) -> str:
        session_id = f"{name}_{datetime.now().isoformat()}"
        self._sessions[session_id] = {
            'name': name,
            'start': datetime.now(),
            'status': 'active',
        }
        print(f"[SESSION] Iniciada: {session_id}")
        return session_id

    def end_session(self, session_id: str) -> None:
        if session_id in self._sessions:
            self._sessions[session_id]['status'] = 'closed'
            self._sessions[session_id]['end'] = datetime.now()
            print(f"[SESSION] Finalizada: {session_id}")

    def list_sessions(self, status: Optional[str] = None) -> List[dict]:
        if status:
            return [s for s in self._sessions.values() if s['status'] == status]
        return list(self._sessions.values())


session_manager = SessionManager()
