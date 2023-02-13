class CryptoModel {
  String? id;
  String? symbol;
  String? name;
  String? image;
  double? current_price;

  CryptoModel(this.id, this.symbol, this.name, this.image, this.current_price);

  CryptoModel.fromJson(Map<String, dynamic> json) {
    id = json["id"];
    symbol = json["symbol"];
    name = json["name"];
    image = json["image"];
    current_price = json["current_price"];
  }
}
