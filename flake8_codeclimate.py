# encoding: utf-8

"""
Flake8 plugin for Code Climate JSON format reporting::

    flake8 --format=codeclimate

"""

import hashlib
import json

from flake8.formatting import base
from pkg_resources import DistributionNotFound, get_distribution

__author__ = 'Ben Lopatin'
__license__ = 'MIT'

try:
    __version__ = get_distribution(__name__).version
except DistributionNotFound:
    # package is not installed
    pass


category_complexity = "Complexity"
category_bug = "Bug Risk"
category_style = "Style"
category_clarity = "Clarity"
category_compatibility = "Compatibility"


error_classes = {
    "C9": {
        "category": category_complexity,
    },
    "E": {
        "category": category_style,
    },
    "E7": {
        "category": category_clarity,
    },
    "E9": {
        "category": category_bug,
    },
    "F4": {
        "category": category_bug,
    },
    "F6": {
        "category": category_bug,
    },
    "F7": {
        "category": category_bug,
    },
    "F8": {
        "category": category_bug,
    },
    "W": {
        "category": category_style,
    },
    "W6": {
        "category": category_compatibility,
    },
}


def error_category(error):
    try:
        return error_classes[error.code]["category"]
    except KeyError:
        try:
            return error_classes[error.code][:2]["category"]
        except KeyError:
            try:
                return error_classes[error.code][:1]["category"]
            except KeyError:
                return category_bug


class JSONFormatter(base.BaseFormatter):
    """Formatter for Code Climate JSON reporting"""

    def create_fingerprint(self, error):
        value = ":".join(str(val) for val in error)
        return hashlib.sha256(value.encode("utf-8")).hexdigest()

    def format(self, error):
        return json.dumps({
            "type": "issue",
            "check_name": error.code,  # TODO map codes to names
            "description": error.text,
            "fingerprint": self.create_fingerprint(error),
            "content": {
                "body": "`{}`".format(error.physical_line),
            },
            "categories": [error_category(error)],
            "location": {
                "path": error.filename,
                "lines": {
                    "begin": error.line_number,
                    "end": error.line_number,
                },
                "positions": {
                    "begin": {
                        "line": error.line_number,
                        "column": error.column_number,
                    },
                    "end": {
                        "line": error.line_number,
                        "column": error.column_number,
                    },
                },

            },
            "remediation_points": None,
            # "severity": Severity,  # TODO map severity
        })
