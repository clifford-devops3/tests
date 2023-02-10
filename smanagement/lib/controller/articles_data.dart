import 'dart:convert';

import 'package:flutter/cupertino.dart';
import 'package:smanagement/models/article_model.dart';
import "package:http/http.dart" as http;

class AlticlesProvider extends ChangeNotifier {
  List<ArticleModel> _articles = <ArticleModel>[];

  List<ArticleModel> get articles => _articles;

  Future<void> getArticles() async {
    const url = "http://localhost:5000/get-articles";
    final uri = Uri.parse(url);
    final response = await http.get(uri);

    if (response.statusCode == 200) {
      final data = jsonDecode(response.body) as Map;


      (data['articles'] as List).forEach(
          (article) => {_articles.add(ArticleModel.fromJson(article))});

      notifyListeners();
    }
  }

  void getAllNews() {
    notifyListeners();
  }
}
