from starlette.requests import Request
import ofjustpy as oj
from starlette.middleware import Middleware
class InitRequestStateMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope['type'] == 'http':
            request = Request(scope)
            # Initialize request.state
            request.state.advanced_demo_bar_selected_btn = None

        await self.app(scope, receive, send)

            
app  = oj.build_app(middlewares=[Middleware(InitRequestStateMiddleware)
                                 ])
