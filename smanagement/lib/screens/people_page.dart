import 'package:flutter/material.dart';
import 'package:flutter/src/foundation/key.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:provider/provider.dart';
import 'package:smanagement/controller/news_data.dart';
import 'package:smanagement/controller/people_data.dart';
import 'package:smanagement/screens/home_page.dart';

class PeoplePage extends StatefulWidget {
  const PeoplePage({Key? key}) : super(key: key);

  @override
  State<PeoplePage> createState() => _PeoplePageState();
}

class _PeoplePageState extends State<PeoplePage> {
  void backHome(BuildContext context) {
    final route = MaterialPageRoute(builder: (context) => HomePage());
    Navigator.push(context, route);
  }

  void addPerson() {
    final body = {"age": 20, "name": "Joseph"};

    context.read<PeopleDataProvider>().addPerson(body);
  }

  @override
  void initState() {
    // TODO: implement initState
    context.read<PeopleDataProvider>().getAllPeople();
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("People")),
      body: Column(
        children: [
          Container(
              child: MaterialButton(
            child: Text("Home page"),
            onPressed: () => {backHome(context)},
          )),
          Container(
              child: MaterialButton(
            child: Text("Add Person"),
            onPressed: () => {addPerson()},
          )),
          Container(
            height: 600,
            child:
                Consumer<PeopleDataProvider>(builder: (context, value, child) {
              return ListView.builder(
                itemCount: value.getPeople.length,
                itemBuilder: (BuildContext context, int index) {
                  return ListTile(
                    title: Text("How are you doing"),
                    subtitle: Text("Am good!!"),
                    trailing: MaterialButton(
                        child: Text("Delete"),
                        onPressed: () =>
                            {value.deletePerson(value.getPeople[index].id!)}),
                  );
                },
              );
            }),
          )
        ],
      ),
    );
  }
}
