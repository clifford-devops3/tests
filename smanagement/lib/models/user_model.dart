class User {
  int? id;
  String? first_name;
  String? last_name;
  String? email;

  User(this.id, this.first_name, this.last_name, this.email);

  User.fromJson(Map<String, dynamic> json) {
    id = json["id"];
    first_name = json["first_name"];
    last_name = json["last_name"];
    email = json["email"];
  }
}
