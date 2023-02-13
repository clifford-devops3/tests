import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:smanagement/controller/articles_data.dart';
import 'package:smanagement/controller/crypto_data.dart';
import 'package:smanagement/controller/forex_data.dart';
import 'package:smanagement/controller/user_data.dart';
import 'package:smanagement/screens/home_page.dart';

void main() {
  runApp(MultiProvider(
    providers: [
      ChangeNotifierProvider(
        create: (context) => AlticlesProvider(),
      ),
      ChangeNotifierProvider(
        create: (context) => UserDataProvider(),
      ),
      ChangeNotifierProvider(create: (context) => ForexDataProvider()),
      ChangeNotifierProvider(create: (context) => CryptoDataProvider())
    ],
    child: MaterialApp(
      home: HomePage(),
      debugShowCheckedModeBanner: false,
    ),
  ));
}
