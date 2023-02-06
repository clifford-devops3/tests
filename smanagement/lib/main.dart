import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:smanagement/controller/news_data.dart';
import 'package:smanagement/controller/people_data.dart';
import 'package:smanagement/screens/home_page.dart';

void main() {
  runApp(MultiProvider(
    providers: [
      ChangeNotifierProvider(
        create: (context) => NewsDataPrivider(),
      ),
      ChangeNotifierProvider(
        create: (context) => PeopleDataProvider(),
      )
    ],
    child: MaterialApp(
      home: HomePage(),
      debugShowCheckedModeBanner: false,
    ),
  ));
}