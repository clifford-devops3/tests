import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:smanagement/controller/articles_data.dart';
import 'package:smanagement/screens/home_page.dart';
import 'package:smanagement/screens/Assets.dart';
import 'package:smanagement/shared/bottom_navigation.dart';

class Articles extends StatefulWidget {
  const Articles({Key? key}) : super(key: key);

  @override
  State<Articles> createState() => _ArticlesState();
}

class _ArticlesState extends State<Articles> {


  @override
  void initState() {
    // TODO: implement initState
    context.read<AlticlesProvider>().getArticles();
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Articles")),
      body: Container(
        child: Consumer<AlticlesProvider>(builder: (context, value, child) {
          return ListView.builder(
              itemCount: value.articles.length,
              itemBuilder: (BuildContext context, int index) {
                int end = value.articles[index].body!.length < 100
                    ? value.articles[index].body!.length
                    : 100;

                String imageurl = value.articles[index].imageurl != null
                    ? value.articles[index].imageurl!
                    : 'https://images.cryptocompare.com/news/default/livebitcoinnews.png?width=250';

                return ListTile(
                  leading: Container(child: Image.network(imageurl)),
                  title: Text(value.articles[index].title!),
                  subtitle: Text(
                      '${value.articles[index].body!.substring(0, end)}...'),
                );
              });
        }),
      ),
      bottomNavigationBar: BottomNavigation(2),
    );
  }
}
