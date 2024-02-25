"""
Having the next helper, please implement a refactor to perform the API call
using one method instead of rewriting the code in the other methods.
"""
import requests


class Helper:

    """Main class to interact with image APIs."""

    DOMAIN = 'http://example.com'
    SEARCH_IMAGES_ENDPOINT = 'search/images'
    GET_IMAGE_ENDPOINT = 'image'
    DOWNLOAD_IMAGE_ENDPOINT = 'downloads/images'

    AUTHORIZATION_TOKEN = {
        'access_token': None,
        'token_type': None,
        'expires_in': 0,
        'refresh_token': None
    }

    def _send_request(
            self, endpoint, method, data=None, params=None):
        """
        Send API request.

        :param endpoint: str, endpoint to request.
        :param method: str, HTTP method.
        :param data: str, data for the request.
        :param params: additional params.

        :return: API response.
        """
        token_type = self.AUTHORIZATION_TOKEN['token_type']
        access_token = self.AUTHORIZATION_TOKEN['access_token']
        headers = {
            'Authorization': f'{token_type} {access_token}',
        }
        url = f'{self.DOMAIN}/{endpoint}'
        response = requests.request(
            method, url, headers=headers, data=data, params=params)
        response.raise_for_status()

        return response

    def search_images(self, **kwargs):
        """
        Search images based on params.

        :param kwargs: Additional params.

        :return: API response.
        """
        return self._send_request(
            self.SEARCH_IMAGES_ENDPOINT, 'GET', params=kwargs)

    def get_image(self, image_id, **kwargs):
        """
        Get image information.

        :param image_id: Image id to retrieve info.
        :param kwargs: Additional params.

        :return: API response.
        """
        return self._send_request(
            f'{self.DOWNLOAD_IMAGE_ENDPOINT}/{image_id}', 'GET', data=kwargs)

    def download_image(self, image_id, **kwargs):
        """
        Download a specific image.

        :param image_id: Image id to download.
        :param kwargs: Additional params.

        :return: API response.
        """
        return self._send_request(
            f'{self.DOWNLOAD_IMAGE_ENDPOINT}/{image_id}', 'POST', data=kwargs)
