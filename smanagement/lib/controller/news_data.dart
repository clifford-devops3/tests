import 'package:flutter/cupertino.dart';

class NewsDataPrivider extends ChangeNotifier {
  String _data = "News Data";
  String get getData => _data;

  void getLatestNews() {
    _data = "Latest News";
    notifyListeners();
  }

  void getAllNews() {
    _data = "All News";
    notifyListeners();
  }
}
