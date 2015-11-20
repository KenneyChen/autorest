# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator 0.13.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Serializer, Deserializer
from msrest.service_client import async_request
from msrest.exceptions import (
    DeserializationError,
    HttpOperationError)

from ..models import *


class implicit(object):

    def __init__(self, client, config, serializer, derserializer):

        self._client = client
        self._serialize = serializer
        self._deserialize = derserializer

        self.config = config

    def _parse_url(self, name, value, datatype):

        try:
            value = self._serialize.serialize_data(value, datatype)

        except ValueError:
            raise ValueError("{} must not be None.".format(name))

        except DeserializationError:
            raise TypeError("{} must be type {}.".format(name, datatype))

        else:
            return value

    @async_request
    def get_required_path(self, path_parameter, custom_headers={}, raw=False, callback=None):
        """

        Test implicitly required path parameter

        :param path_parameter:
        :param custom_headers: headers that will be added to the request
        :param raw: returns the direct response alongside the deserialized
        response
        :param callback: if provided, the call will run asynchronously and
        call the callback when complete.  When specified the function returns
        a concurrent.futures.Future
        :type path_parameter: str
        :type custom_headers: dict
        :type raw: boolean
        :type callback: Callable[[concurrent.futures.Future], None] or None
        :rtype: object or (object, requests.response) or
        concurrent.futures.Future
        """

        # Construct URL
        url = '/reqopt/implicit/required/path/{pathParameter}'
        path_format_arguments = {
            'pathParameter': self._parse_url("path_parameter", path_parameter, 'str', False)}
        url = url.format(**path_format_arguments)

        # Construct parameters
        query = {}

        # Construct headers
        headers = {}
        headers.update(custom_headers)
        headers['Content-Type'] = 'application/json; charset=utf-8'

        # Construct and send request
        request = self._client.get(url, query)
        response = self._client.send(request, headers)

        if reponse.status_code < 200 or reponse.status_code >= 300:
            raise ErrorException(self._deserialize, response)

        if raw:
            return None, response

    @async_request
    def put_optional_query(self, query_parameter, custom_headers={}, raw=False, callback=None):
        """

        Test implicitly optional query parameter

        :param query_parameter:
        :param custom_headers: headers that will be added to the request
        :param raw: returns the direct response alongside the deserialized
        response
        :param callback: if provided, the call will run asynchronously and
        call the callback when complete.  When specified the function returns
        a concurrent.futures.Future
        :type query_parameter: str or none
        :type custom_headers: dict
        :type raw: boolean
        :type callback: Callable[[concurrent.futures.Future], None] or None
        :rtype: None or (None, requests.response) or concurrent.futures.Future
        """

        # Construct URL
        url = '/reqopt/implicit/optional/query'

        # Construct parameters
        query = {}
        if query_parameter is not None:
            query['queryParameter'] = self._parse_url("query_parameter", query_parameter, 'str', False)

        # Construct headers
        headers = {}
        headers.update(custom_headers)
        headers['Content-Type'] = 'application/json; charset=utf-8'

        # Construct and send request
        request = self._client.put(url, query)
        response = self._client.send(request, headers)

        if response.status_code not in [200]:
            raise ErrorException(self._deserialize, response)

        if raw:
            return None, response

    @async_request
    def put_optional_header(self, query_parameter, custom_headers={}, raw=False, callback=None):
        """

        Test implicitly optional header parameter

        :param query_parameter:
        :param custom_headers: headers that will be added to the request
        :param raw: returns the direct response alongside the deserialized
        response
        :param callback: if provided, the call will run asynchronously and
        call the callback when complete.  When specified the function returns
        a concurrent.futures.Future
        :type query_parameter: str or none
        :type custom_headers: dict
        :type raw: boolean
        :type callback: Callable[[concurrent.futures.Future], None] or None
        :rtype: None or (None, requests.response) or concurrent.futures.Future
        """

        # Construct URL
        url = '/reqopt/implicit/optional/header'

        # Construct parameters
        query = {}

        # Construct headers
        headers = {}
        if query_parameter is not None:
            headers['queryParameter'] = self._serialize.serialize_data(query_parameter, 'str')
        headers.update(custom_headers)
        headers['Content-Type'] = 'application/json; charset=utf-8'

        # Construct and send request
        request = self._client.put(url, query)
        response = self._client.send(request, headers)

        if response.status_code not in [200]:
            raise ErrorException(self._deserialize, response)

        if raw:
            return None, response

    @async_request
    def put_optional_body(self, body_parameter, custom_headers={}, raw=False, callback=None):
        """

        Test implicitly optional body parameter

        :param body_parameter:
        :param custom_headers: headers that will be added to the request
        :param raw: returns the direct response alongside the deserialized
        response
        :param callback: if provided, the call will run asynchronously and
        call the callback when complete.  When specified the function returns
        a concurrent.futures.Future
        :type body_parameter: str or none
        :type custom_headers: dict
        :type raw: boolean
        :type callback: Callable[[concurrent.futures.Future], None] or None
        :rtype: None or (None, requests.response) or concurrent.futures.Future
        """

        # Construct URL
        url = '/reqopt/implicit/optional/body'

        # Construct parameters
        query = {}

        # Construct headers
        headers = {}
        headers.update(custom_headers)
        headers['Content-Type'] = 'application/json; charset=utf-8'

        # Construct body
        content = self._serialize(body_parameter, 'str')

        # Construct and send request
        request = self._client.put(url, query)
        response = self._client.send(request, headers, content)

        if response.status_code not in [200]:
            raise ErrorException(self._deserialize, response)

        if raw:
            return None, response

    @async_request
    def get_required_global_path(self, custom_headers={}, raw=False, callback=None):
        """

        Test implicitly required path parameter

        :param custom_headers: headers that will be added to the request
        :param raw: returns the direct response alongside the deserialized
        response
        :param callback: if provided, the call will run asynchronously and
        call the callback when complete.  When specified the function returns
        a concurrent.futures.Future
        :type custom_headers: dict
        :type raw: boolean
        :type callback: Callable[[concurrent.futures.Future], None] or None
        :rtype: object or (object, requests.response) or
        concurrent.futures.Future
        """

        # Construct URL
        url = '/reqopt/global/required/path/{required-global-path}'
        path_format_arguments = {
            'required-global-path': self._parse_url("self.config.required_global_path", self.config.required_global_path, 'str', False)}
        url = url.format(**path_format_arguments)

        # Construct parameters
        query = {}

        # Construct headers
        headers = {}
        headers.update(custom_headers)
        headers['Content-Type'] = 'application/json; charset=utf-8'

        # Construct and send request
        request = self._client.get(url, query)
        response = self._client.send(request, headers)

        if reponse.status_code < 200 or reponse.status_code >= 300:
            raise ErrorException(self._deserialize, response)

        if raw:
            return None, response

    @async_request
    def get_required_global_query(self, custom_headers={}, raw=False, callback=None):
        """

        Test implicitly required query parameter

        :param custom_headers: headers that will be added to the request
        :param raw: returns the direct response alongside the deserialized
        response
        :param callback: if provided, the call will run asynchronously and
        call the callback when complete.  When specified the function returns
        a concurrent.futures.Future
        :type custom_headers: dict
        :type raw: boolean
        :type callback: Callable[[concurrent.futures.Future], None] or None
        :rtype: object or (object, requests.response) or
        concurrent.futures.Future
        """

        # Construct URL
        url = '/reqopt/global/required/query'

        # Construct parameters
        query = {}
        if self.config.required_global_query is not None:
            query['required-global-query'] = self._parse_url("self.config.required_global_query", self.config.required_global_query, 'str', False)

        # Construct headers
        headers = {}
        headers.update(custom_headers)
        headers['Content-Type'] = 'application/json; charset=utf-8'

        # Construct and send request
        request = self._client.get(url, query)
        response = self._client.send(request, headers)

        if reponse.status_code < 200 or reponse.status_code >= 300:
            raise ErrorException(self._deserialize, response)

        if raw:
            return None, response

    @async_request
    def get_optional_global_query(self, custom_headers={}, raw=False, callback=None):
        """

        Test implicitly optional query parameter

        :param custom_headers: headers that will be added to the request
        :param raw: returns the direct response alongside the deserialized
        response
        :param callback: if provided, the call will run asynchronously and
        call the callback when complete.  When specified the function returns
        a concurrent.futures.Future
        :type custom_headers: dict
        :type raw: boolean
        :type callback: Callable[[concurrent.futures.Future], None] or None
        :rtype: object or (object, requests.response) or
        concurrent.futures.Future
        """

        # Construct URL
        url = '/reqopt/global/optional/query'

        # Construct parameters
        query = {}
        if self.config.optional_global_query is not None:
            query['optional-global-query'] = self._parse_url("self.config.optional_global_query", self.config.optional_global_query, 'int', False)

        # Construct headers
        headers = {}
        headers.update(custom_headers)
        headers['Content-Type'] = 'application/json; charset=utf-8'

        # Construct and send request
        request = self._client.get(url, query)
        response = self._client.send(request, headers)

        if reponse.status_code < 200 or reponse.status_code >= 300:
            raise ErrorException(self._deserialize, response)

        if raw:
            return None, response
