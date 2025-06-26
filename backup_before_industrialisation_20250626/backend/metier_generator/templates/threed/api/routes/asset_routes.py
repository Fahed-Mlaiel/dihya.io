"""
Routes API métier threed (Flask)
"""

from flask import Blueprint, request, jsonify
from ..controllers.asset_controller import AssetController

asset_routes = Blueprint("asset_routes", __name__)


@asset_routes.route("/assets", methods=["GET"])
def list_assets():
    return jsonify(AssetController.list_assets())


@asset_routes.route("/assets", methods=["POST"])
def create_asset():
    return jsonify(AssetController.create_asset(request.json))


@asset_routes.route("/assets/<int:id>", methods=["GET"])
def get_asset(id):
    return jsonify(AssetController.get_asset(id))


@asset_routes.route("/assets/<int:id>", methods=["DELETE"])
def delete_asset(id):
    return jsonify(AssetController.delete_asset(id))
