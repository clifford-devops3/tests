import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:flutter/src/foundation/key.dart';
import 'package:flutter/src/widgets/framework.dart';
import 'package:smanagement/screens/crypto_page.dart';
import 'package:smanagement/screens/forex_page.dart';

class MarketTabs extends StatefulWidget {
  final int activeIndex;
  const MarketTabs(this.activeIndex, {Key? key}) : super(key: key);

  @override
  State<MarketTabs> createState() => _MarketTabsState();
}

class _MarketTabsState extends State<MarketTabs>
    with SingleTickerProviderStateMixin {
  late TabController _tabController;
  @override
  void initState() {
    _tabController =
        TabController(vsync: this, length: 3, initialIndex: widget.activeIndex);
    // TODO: implement initState
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return TabBar(
      controller: _tabController,
      onTap: (index) => {tabMenu(context, index)},
      tabs: [
        Tab(
          child: Text("Forex", style: TextStyle(color: Colors.black)),
        ),
        Tab(
          child: Text("Crypto", style: TextStyle(color: Colors.black)),
        ),
        Tab(
          child: Text("Favourite", style: TextStyle(color: Colors.black)),
        ),
      ],
    );
  }

  tabMenu(BuildContext context, int index) {
    if (index == 0) {
      final route = MaterialPageRoute(builder: (context) => ForexPage());
      Navigator.pushReplacement(context, route);
    } else if (index == 1) {
      final route = MaterialPageRoute(builder: (context) => CryptoPage());
      Navigator.pushReplacement(context, route);
    }
  }
}
