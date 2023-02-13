import 'dart:convert';

import 'package:flutter/cupertino.dart';
import 'package:smanagement/models/user_model.dart';
import "package:http/http.dart" as http;

class UserDataProvider extends ChangeNotifier {
  List<User> _users = <User>[];
  final User _user = User(null, null, null, null);
  
  List<User> users = <User>[];
  User get user => _user;

  Future<void> getUser() async {
    const url = "http://localhost:5000";
    final uri = Uri.parse(url);

    final response = await http.get(uri);

    if (response.statusCode == 200) {
      _users = [];
      final data = jsonDecode(response.body) as Map;
      (data['people'] as List)
          .forEach((person) => {_users.add(User.fromJson(person))});
      notifyListeners();
    }
  }

  Future<void> getAllPeople() async {
    const url = "http://localhost:5000";
    final uri = Uri.parse(url);

    final response = await http.get(uri);

    if (response.statusCode == 200) {
      _users = [];
      final data = jsonDecode(response.body) as Map;
      (data['people'] as List)
          .forEach((person) => {_users.add(User.fromJson(person))});
      notifyListeners();
    }
  }

  Future<void> addPerson(Map<String, Object> body) async {
    const url = "http://localhost:5000/add-person";
    final uri = Uri.parse(url);

    final response = await http.post(uri,
        headers: {'Content-Type': 'application/json'}, body: jsonEncode(body));

    if (response.statusCode == 200) {
      _users = [];
      final data = jsonDecode(response.body) as Map;
      (data['people'] as List)
          .forEach((person) => {_users.add(User.fromJson(person))});
      notifyListeners();
    }
  }

  Future<void> deletePerson(int id) async {
    final url = "http://localhost:5000/delete-person/${id}";
    final uri = Uri.parse(url);
    final response = await http.delete(uri);

    if (response.statusCode == 200) {
      _users = [];
      final data = jsonDecode(response.body) as Map;

      (data['people'] as List)
          .forEach((person) => {_users.add(User.fromJson(person))});

      notifyListeners();
    }
  }
}
