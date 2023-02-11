class ForexModel {
  String? currency;
  String? currency_code;
  String? country;
  String? country_code;
  double? rate;

  ForexModel(this.currency, this.currency_code, this.country, this.country_code,
      this.rate);

  ForexModel.fromJson(Map<String, dynamic> json) {
    currency = json['currency'];
    currency_code = json['currency_code'];
    country = json['country'];
    country_code = json['country_code'];
    rate = json['rate'];
  }
}
