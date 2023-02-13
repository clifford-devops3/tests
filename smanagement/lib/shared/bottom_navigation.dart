import 'package:flutter/material.dart';
import 'package:smanagement/screens/Assets.dart';
import 'package:smanagement/screens/Feeds.dart';
import 'package:smanagement/screens/forex_page.dart';
import 'package:smanagement/screens/home_page.dart';
import 'package:smanagement/screens/articles.dart';

class BottomNavigation extends StatelessWidget {
  final int selected;
  const BottomNavigation(this.selected, {Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return BottomNavigationBar(
        type: BottomNavigationBarType.fixed,
        selectedFontSize: 11,
        currentIndex: selected,
        selectedIconTheme: IconThemeData(color: Colors.cyan[300], size: 24),
        selectedLabelStyle: TextStyle(fontWeight: FontWeight.bold),
        unselectedIconTheme: IconThemeData(
          color: Colors.grey[300],
        ),
        items: [
          BottomNavigationBarItem(
            icon: Icon(
              Icons.feed_outlined,
            ),
            label: "Favourite",
          ),
          BottomNavigationBarItem(
            icon: Icon(
              Icons.align_horizontal_left_outlined,
            ),
            label: "Market",
          ),
          BottomNavigationBarItem(
            icon: Icon(
              Icons.data_thresholding_sharp,
            ),
            label: "Articles",
          ),
          BottomNavigationBarItem(
            icon: Icon(
              Icons.chat_bubble_outline_rounded,
            ),
            label: "Feeds",
          ),
          BottomNavigationBarItem(
            icon: Icon(
              Icons.diamond,
            ),
            label: "Assets",
          ),
        ],
        onTap: (index) => {openPage(context, index)});
  }

  void openPage(BuildContext context, int index) {
    if (index == 0) {
      final route = MaterialPageRoute(builder: (context) => HomePage());
      Navigator.pushReplacement(context, route);
    } else if (index == 1) {
      final route = MaterialPageRoute(builder: (context) => ForexPage()); //
      Navigator.pushReplacement(context, route);
    } else if (index == 2) {
      final route = MaterialPageRoute(builder: (context) => Articles());
      Navigator.pushReplacement(context, route);
    } else if (index == 3) {
      final route = MaterialPageRoute(builder: (context) => Feeds());
      Navigator.pushReplacement(context, route);
    } else if (index == 4) {
      final route = MaterialPageRoute(builder: (context) => Assets());
      Navigator.pushReplacement(context, route);
    }
  }
}
