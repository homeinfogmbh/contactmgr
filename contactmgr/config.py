"""Configuration file parsing."""

from configlib import loadcfg


__all__ = ["CONFIG"]


CONFIG = loadcfg("contactmgr.conf")
