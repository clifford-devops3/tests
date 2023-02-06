import 'package:flutter/material.dart';
import 'package:flutter/src/foundation/key.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:provider/provider.dart';
import 'package:smanagement/controller/news_data.dart';
import 'package:smanagement/screens/latest_news.dart';
import 'package:smanagement/screens/people_page.dart';

class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  void latestNews(BuildContext context) {
    context.read<NewsDataPrivider>().getLatestNews();
    final route = MaterialPageRoute(builder: (context) => LatestNews());
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
          return Text(
            value.getData.toString(),
          );
        }),
        MaterialButton(
          onPressed: () => {latestNews(context)},
          child: Text("Latest News"),
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
