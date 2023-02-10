import 'dart:convert';

import 'package:flutter/cupertino.dart';
import 'package:smanagement/models/person_model.dart';
import "package:http/http.dart" as http;

class PeopleDataProvider extends ChangeNotifier {
  List<Person> _people = [];

  List<Person> get getPeople => _people;

  Future<void> getAllPeople() async {
    const url = "http://localhost:5000";
    final uri = Uri.parse(url);

    final response = await http.get(uri);

    if (response.statusCode == 200) {
      _people = [];
      final data = jsonDecode(response.body) as Map;
      (data['people'] as List)
          .forEach((person) => {_people.add(Person.fromJson(person))});
      notifyListeners();
    }
  }

  Future<void> addPerson(Map<String, Object> body) async {
    const url = "http://localhost:5000/add-person";
    final uri = Uri.parse(url);

    final response = await http.post(uri,
        headers: {'Content-Type': 'application/json'}, body: jsonEncode(body));

    if (response.statusCode == 200) {
      _people = [];
      final data = jsonDecode(response.body) as Map;
      (data['people'] as List)
          .forEach((person) => {_people.add(Person.fromJson(person))});
      notifyListeners();
    }
  }

  Future<void> deletePerson(int id) async {
    final url = "http://localhost:5000/delete-person/${id}";
    final uri = Uri.parse(url);
    final response = await http.delete(uri);

    if (response.statusCode == 200) {
      _people = [];
      final data = jsonDecode(response.body) as Map;

      (data['people'] as List)
          .forEach((person) => {_people.add(Person.fromJson(person))});

      notifyListeners();
    }
  }
}
