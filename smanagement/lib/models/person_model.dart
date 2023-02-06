class Person {
  int? id;
  String? name;
  int? age;

  Person(this.id, this.name, this.age);

  Person.fromJson(Map<String, dynamic> json) {
    id = json["id"];
    name = json["name"];
    age = json["age"];
  }
}
