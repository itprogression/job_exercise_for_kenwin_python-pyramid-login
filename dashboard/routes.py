def includeme(config):
    config.add_static_view('assets', 'static/assets', cache_max_age=3600)
    config.add_static_view('images', 'static/images', cache_max_age=3600)
    config.add_route('home', '/')
    config.add_route('dashboard', '/dashboard')
    config.add_route('login', '/login')
    config.add_route('logout', '/logout')