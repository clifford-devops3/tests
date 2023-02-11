import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:smanagement/controller/forex_data.dart';
import 'package:smanagement/shared/bottom_navigation.dart';

class Market extends StatefulWidget {
  const Market({Key? key}) : super(key: key);

  @override
  State<Market> createState() => _MarketState();
}

class _MarketState extends State<Market> {
  @override
  void initState() {
    // TODO: implement initState
    context.read<ForexDataProvider>().getForex();
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      initialIndex: 1,
      length: 3,
      child: Scaffold(
        appBar: AppBar(title: Text("Market")),
        body: Column(
          children: [
            Expanded(
                flex: 1,
                child: Container(
                  child: TabBar(tabs: [
                    Tab(
                      child:
                          Text("Forex", style: TextStyle(color: Colors.black)),
                    ),
                    Tab(
                      child:
                          Text("Crypto", style: TextStyle(color: Colors.black)),
                    ),
                    Tab(
                      child: Text("Favourite",
                          style: TextStyle(color: Colors.black)),
                    ),
                  ]),
                )),
            Expanded(
              flex: 9,
              child: Container(
                child: Consumer<ForexDataProvider>(
                    builder: (context, value, child) {
                  return ListView.builder(
                      itemCount: value.forex.length,
                      itemBuilder: (BuildContext context, int index) {
                        return ListTile(
                          leading: Text(value.forex[index].currency_code!),
                          title: Text(value.forex[index].currency!),
                          subtitle: Text(value.forex[index].country!),
                          trailing: Text(value.forex[index].rate!.toString()),
                        );
                      });
                }),
              ),
            ),
          ],
        ),
        bottomNavigationBar: BottomNavigation(1),
      ),
    );
  }
}
