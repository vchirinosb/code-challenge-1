"""
A video transcoder was implemented with different presets to process different
videos in the application. The videos should be encoded with a given
configuration done by this function. Can you explain what this function is
detecting from the params and returning based in its conditionals?
"""
import unittest


def fn(config, w, h):
    """
    Get list of presets based on a video configuration(config), width(w) and
    height(h).

    :param config: Dict, contains three different configurations for 'p', 'l',
        's'.
    :param w: int, width value.
    :param h: int, height value.

    :return: List of presets based on the aspect ratio(ar) and width
        value(w).
    """
    v = None
    # Aspect ratio(ar) calculated based on the width(w) and height(h) input
    # values.
    ar = w / h

    if ar < 1:
        # If aspect ratio(ar) is less than 1, then presets are obtained from
        # 'p' value from the configuration only if the width is less or equal
        # to the provided width('w') value.
        v = [r for r in config['p'] if r['width'] <= w]
    elif ar > 4 / 3:
        # If aspect ratio(ar) is greater than 4/3, then presets are obtained
        # from 'l' value from the configuration only if the width is less or
        # equal to the provided width('w') value.
        v = [r for r in config['l'] if r['width'] <= w]
    else:
        # For any other aspect ratio(ar) values, between 1 and 4/3, then
        # presets are obtained from 's' value from the configuration only if
        # the width is less or equal to the provided width('w') value.
        v = [r for r in config['s'] if r['width'] <= w]

    # List 'v' to be returned corresponds to the list of presets obtained based
    # on the aspect ratio(ar) and width input value(w).
    return v


class VideoTranscoderTest(unittest.TestCase):

    """Test cases for Video Transcoder."""

    def test_fn(self):
        """Test fn method."""
        config = {
            'p': [{'width': 480}, {'width': 720}],
            'l': [{'width': 720}, {'width': 1080}],
            's': [{'width': 320}, {'width': 480}]
        }

        # Test aspect ratio(ar) less than 1.
        # ar = 640/800 = 0.8 < 1
        self.assertEqual(
            fn(config, 640, 800),
            [{'width': 480}]
        )

        # Test aspect ratio(ar) greater than 4/3.
        # ar = 1920/1080 = 1.7 > 4/3
        self.assertEqual(
            fn(config, 1920, 1080),
            [{'width': 720}, {'width': 1080}]
        )

        # Test other aspect ratio(ar) values, e.g. between 1 and 4/3.
        # ar = 800/600 = 1.3; 1 < 1.3 < 4/3
        self.assertEqual(
            fn(config, 800, 600),
            [{'width': 320}, {'width': 480}]
        )


if __name__ == '__main__':
    unittest.main()
