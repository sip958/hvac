"""Collection of classes for various Vault auth methods."""


from hvac.api.auth.azure import Azure
from hvac.api.auth.gcp import Gcp
from hvac.api.auth.github import Github
from hvac.api.auth.ldap import Ldap
from hvac.api.auth.mfa import Mfa

__all__ = (
    'Azure',
    'Github',
    'Gcp',
    'Ldap',
    'Mfa',
)
