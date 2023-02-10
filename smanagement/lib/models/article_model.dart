class ArticleModel {
  String? id;
  String? title;
  String? url;
  String? body;
  String? guid;
  String? tags;
  String? categories;
  String? imageurl;

  ArticleModel(this.id, this.title, this.url, this.body, this.guid, this.tags,
      this.categories, this.imageurl);

  ArticleModel.fromJson(Map<String, dynamic> json) {
    id = json['id'];
    title = json['title'];
    url = json['url'];
    body = json['body'];
    guid = json['guid'];
    tags = json['tags'];
    categories = json['categories'];
    imageurl = json['imageurl'];
  }
}
