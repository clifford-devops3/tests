import 'package:flutter/material.dart';
import 'package:flutter/src/foundation/key.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:provider/provider.dart';
import 'package:smanagement/controller/articles_data.dart';
import 'package:smanagement/controller/people_data.dart';
import 'package:smanagement/screens/home_page.dart';
import 'package:smanagement/shared/bottom_navigation.dart';

class Assets extends StatefulWidget {
  const Assets({Key? key}) : super(key: key);

  @override
  State<Assets> createState() => _AssetsState();
}

class _AssetsState extends State<Assets> {
  @override
  void initState() {
    // TODO: implement initState
    context.read<PeopleDataProvider>().getAllPeople();
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(
          "Assets",
          style: TextStyle(color: Color.fromARGB(255, 47, 47, 47)),
        ),
        elevation: 0,
        backgroundColor: Color.fromARGB(255, 244, 254, 255),
      ),
      backgroundColor: Color.fromARGB(255, 247, 251, 251),
      body: Container(
        child: Consumer<PeopleDataProvider>(builder: (context, value, child) {
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
      ),
      bottomNavigationBar: BottomNavigation(4),
    );
  }
}
