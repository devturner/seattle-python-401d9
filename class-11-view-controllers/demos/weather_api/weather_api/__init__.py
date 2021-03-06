from pyramid.config import Configurator


def main(global_config, **settings):
    """ This function returns a Pyramid WSGI application.
    """
    # import pdb; pdb.set_trace()
    config = Configurator(settings=settings)
    config.include('pyramid_restful')
    config.include('.models')
    config.include('.routes')
    config.scan()
    return config.make_wsgi_app()
