"""
Contrôleur métier threed (Python)
"""


class AssetController:
    assets = []

    @staticmethod
    def list_assets():
        return AssetController.assets

    @staticmethod
    def create_asset(data):
        AssetController.assets.append(data)
        return data

    @staticmethod
    def get_asset(id):
        for a in AssetController.assets:
            if a.get("id") == id:
                return a
        return {}

    @staticmethod
    def delete_asset(id):
        before = len(AssetController.assets)
        AssetController.assets = [
            a for a in AssetController.assets if a.get("id") != id
        ]
        return {"deleted": len(AssetController.assets) < before}
