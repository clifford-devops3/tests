import 'package:flutter/material.dart';

class HomePage extends StatelessWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Container(
        child: ListView(children: [
          ListTile(
            leading: Icon(
              Icons.agriculture_rounded,
              color: Colors.deepOrangeAccent[300],
            ),
            title: Container(
              height: 40,
              width: 40,
              decoration: BoxDecoration(
                  color: Colors.deepOrange,
                  borderRadius: BorderRadius.all(Radius.circular(20))),
              child: Center(
                child: Text(
                  "App",
                  style: TextStyle(color: Colors.white),
                ),
              ),
            ),
            subtitle: Text('Sub title'),
            trailing: PopupMenuButton(itemBuilder: (context) {
              return [
                PopupMenuItem(child: Text("Edit")),
              ];
            }),
          ),
        ]),
      ),
    );
  }
}
