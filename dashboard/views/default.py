import logging
log = logging.getLogger(__name__)

from pyramid.httpexceptions import HTTPFound
from pyramid.security import (
    remember,
    forget,
    )

from pyramid.view import (
    view_config,
    view_defaults,
    forbidden_view_config
    )

from ..security import (
    USERS,
    check_password
)


@view_defaults(renderer='dashboard:templates/home.pt')
class TutorialViews:
    def __init__(self, request):
        self.request = request
        self.logged_in = request.authenticated_userid

    @view_config(route_name='home')
    def home(self):
        log.debug('In home view')
        return {'name': 'Home View'}

    @view_config(route_name='dashboard', permission='edit', renderer='dashboard:templates/dashboard.pt')
    def dashboard(self):
        log.debug('In Dashboard view')
        return {'name': 'Dashboard View'}

    @view_config(route_name='login', renderer='dashboard:templates/login.pt')
    @forbidden_view_config(renderer='dashboard:templates/login.pt')
    def login(self):
        log.debug('In login view')
        request = self.request
        login_url = request.route_url('login')
        referrer = request.url
        if referrer == login_url:
            referrer = '/'  # never use login form itself as came_from
        came_from = request.params.get('came_from', referrer)
        message = ''
        login = ''
        password = ''
        if 'form.submitted' in request.params:
            login = request.params['login']
            password = request.params['password']
            hashed_pw = USERS.get(login)
            if hashed_pw and check_password(password, hashed_pw):
                headers = remember(request, login)
                return HTTPFound(location=came_from,
                                 headers=headers)
            message = 'Failed login'

        return dict(
            name='Login',
            message=message,
            url=request.application_url + '/login',
            came_from=came_from,
            login=login,
            password=password,
        )

    @view_config(route_name='logout')
    def logout(self):
        log.debug('In logout view')
        request = self.request
        headers = forget(request)
        url = request.route_url('home')
        return HTTPFound(location=url,
                         headers=headers)