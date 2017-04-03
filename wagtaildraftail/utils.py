from __future__ import absolute_import, unicode_literals

from django.template.defaultfilters import filesizeformat


def get_document_meta(document):
    """
    :type document: wagtail.wagtaildocs.models.Document (or subclass)
    :param document: the document
    :rtype: dict
    :return: the document size and extension
    """

    return {
        'extension': document.file_extension.lower(),
        'size': filesizeformat(document.file.size)
    }
