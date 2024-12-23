import json

class Coordinate:
    def __init__(self, longitude: str, latitude: str):
        """
        Constructor for the Coordinate class.
        
        :param longitude: Longitude as a string.
        :param latitude: Latitude as a string.
        """
        self._longitude = longitude
        self._latitude = latitude

    def get_longitude(self) -> str:
        """
        Returns the longitude of the coordinate.
        
        :return: Longitude as a string.
        """
        return self._longitude

    def get_latitude(self) -> str:
        """
        Returns the latitude of the coordinate.
        
        :return: Latitude as a string.
        """
        return self._latitude

    def to_json(self) -> dict:
        """
        Converts the Coordinate instance to a JSON-compatible dictionary.
        
        :return: Dictionary with longitude and latitude.
        """
        return {
            "longitude": self._longitude,
            "latitude": self._latitude
        }

    @classmethod
    def from_json(cls, data: dict) -> 'Coordinate':
        """
        Creates a Coordinate instance from a JSON-compatible dictionary.
        
        :param data: Dictionary containing longitude and latitude.
        :return: A new Coordinate instance.
        """
        return cls(
            longitude=data.get("longitude", ""),
            latitude=data.get("latitude", "")
        )

    def __repr__(self) -> str:
        """
        Returns a string representation of the Coordinate instance.
        
        :return: String representation of the coordinate.
        """
        return f"Coordinate(longitude='{self._longitude}', latitude='{self._latitude}')"
