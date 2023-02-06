import 'package:flutter/material.dart';
import 'package:flutter/src/foundation/key.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:provider/provider.dart';
import 'package:smanagement/controller/news_data.dart';
import 'package:smanagement/screens/home_page.dart';
import 'package:smanagement/screens/people_page.dart';

class LatestNews extends StatefulWidget {
  const LatestNews({Key? key}) : super(key: key);

  @override
  State<LatestNews> createState() => _LatestNewsState();
}

class _LatestNewsState extends State<LatestNews> {
  void allNews(BuildContext context) {
    context.read<NewsDataPrivider>().getAllNews();
    final route = MaterialPageRoute(builder: (context) => HomePage());
    Navigator.push(context, route);
  }

  void getAllPeople(BuildContext context) {
    final route = MaterialPageRoute(builder: (context) => PeoplePage());
    Navigator.push(context, route);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Column(children: [
        Consumer<NewsDataPrivider>(builder: (context, value, child) {
          return Text(value.getData.toString());
        }),
        MaterialButton(
          onPressed: () => {allNews(context)},
          child: Text("All News"),
        ),
        MaterialButton(
          onPressed: () => {
            getAllPeople(context),
          },
          child: Text("All Peole"),
        )
      ]),
    );
  }
}
