#!/usr/bin/python3
"""index"""
from api.v1.views import app_views
from flask import json, jsonify, Response


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """returns API status"""
    return Response(
            json.dumps({"status": "OK"}, indent=2) + "\n",
            mimetype='application/json'
            )
