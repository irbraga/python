#!/usr/bin/python
# -*- coding: utf-8 -*-


def create():
    """
        Creates a pydblite database in memory.
        :return: Base class
    """
    from pydblite.pydblite import Base

    db = Base("temp-db", save_to_file=False)

    db.create("hash", "path")

    return db
