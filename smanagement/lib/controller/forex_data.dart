import 'dart:convert';

import 'package:flutter/cupertino.dart';
import 'package:smanagement/models/forex_model.dart';
import "package:http/http.dart" as http;

class ForexDataProvider extends ChangeNotifier {
  List<ForexModel> _forex = <ForexModel>[];
  List<ForexModel> get forex => _forex;

  Future<void> getForex() async {
    final uri = Uri.parse("http://localhost:5000/fetch-forex");

    final response = await http.get(uri);

    if (response.statusCode == 200) {
      _forex = [];
      final data = jsonDecode(response.body) as Map;

      (data['forex'] as List).forEach((element) {
        _forex.add(ForexModel.fromJson(element));
      });
      notifyListeners();
    }
  }
}
