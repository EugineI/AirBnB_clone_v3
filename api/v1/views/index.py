#!/usr/bin/python3
"""index"""
from api.v1.views import app_views
from flask import json, jsonify, Response
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """returns API status"""
    return Response(
            json.dumps({"status": "OK"}, indent=2) + "\n",
            mimetype='application/json'
            )

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """Retrieves number of objects by type"""
    stats_data = {
            "amenities": storage.count("Amenity"),
            "cities": storage.count("City"),
            "places": storage.count("Place"),
            "reviews": storage.count("Review"),
            "states": storage.count("State"),
            "users": storage.count("User")
            }
    return jsonify(stats_data)
