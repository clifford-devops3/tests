import 'dart:convert';

import 'package:flutter/cupertino.dart';
import 'package:smanagement/models/crypto_model.dart';
import "package:http/http.dart" as http;

class CryptoDataProvider extends ChangeNotifier {
  List<CryptoModel> _cryptos = <CryptoModel>[];
  List<CryptoModel> get cryptos => _cryptos;

  Future<void> getCrypto() async {
    final uri = Uri.parse("http://localhost:5000/get-crypto");
    final response = await http.get(uri);

    if (response.statusCode == 200) {
      _cryptos = <CryptoModel>[];
      final data = jsonDecode(response.body) as Map;

      (data['crypto'] as List)
          .forEach((crypto) => {_cryptos.add(CryptoModel.fromJson(crypto))});

      notifyListeners();
    }
  }
}
