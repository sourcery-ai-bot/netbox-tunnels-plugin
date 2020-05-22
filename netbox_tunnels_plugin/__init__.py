from extras.plugins import PluginConfig


class TunnelConfig(PluginConfig):
    """This class defines attributes for the NetBox Tunnels Plugin."""

    name = 'netbox_tunnels_plugin'
    verbose_name = 'Tunnels'
    description = 'Netbox Tunnels Plugin'
    version = '0.0.1'
    base_url = 'tunnels'
    author = 'Justin Drew'
    author_email = 'jdrew82@gmail.com'
    required_settings = []
    default_settings = {}
    caching_config = {}


config = TunnelConfig