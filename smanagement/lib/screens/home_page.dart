import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:smanagement/controller/articles_data.dart';
import 'package:smanagement/screens/articles.dart';
import 'package:smanagement/screens/Assets.dart';
import 'package:smanagement/shared/bottom_navigation.dart';

class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Crypto News"),
      ),
      body: Column(children: [
        Container(
          height: 500,
          child: ListView.builder(
            itemCount: 2,
            itemBuilder: (BuildContext content, int index) {
              return ListTile(
                leading: Container(
                    child: Image.network(
                        "https://www.cryptocompare.com/cdn-cgi/mirage/d43b10cc9ab8f0e77bde5ef60decf293d19dc8a3ef35b5b8ffa4b4eafc2a7dce/1280/media/43977197/b2b.jpg?width=350")),
                title: Text("What Types of Crypto Derivatives Are The… "),
                subtitle: Text(
                    "In the traditional market, a derivatives contract refers to a type of financial instrument that tracks the price of an underlying asset, allowing …"),
              );
            },
          ),
        ),
      ]),
      bottomNavigationBar: BottomNavigation(0),
    );
  }
}
