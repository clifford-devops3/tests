import 'package:flutter/material.dart';
import 'package:google_mlkit_smart_reply/google_mlkit_smart_reply.dart';

class HomePage extends StatefulWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  @override
  void initState() {
    // TODO: implement initState
    super.initState();

    final DateTime date = DateTime.now();
    const message = "How are you doing?";
    final timestamp = date.millisecondsSinceEpoch;

    getReplies(message, timestamp);
  }

  Future<void> getReplies(String message, int timestamp) async {
    final smartReply = SmartReply();

    smartReply.addMessageToConversationFromLocalUser(message, timestamp);

    final response = await smartReply.suggestReplies();
    for (final suggestion in response.suggestions) {
      print(suggestion);
    }
    // smartReply.close();
    print(message);
  }

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
