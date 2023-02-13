import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:smanagement/controller/forex_data.dart';
import 'package:smanagement/screens/crypto_page.dart';
import 'package:smanagement/shared/bottom_navigation.dart';
import 'package:smanagement/shared/market_tabs.dart';

class ForexPage extends StatefulWidget {
  const ForexPage({Key? key}) : super(key: key);

  @override
  State<ForexPage> createState() => _ForexPageState();
}

class _ForexPageState extends State<ForexPage> {
  @override
  void initState() {
    // TODO: implement initState
    context.read<ForexDataProvider>().getForex();
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Forex")),
      body: Column(
        children: [
          Expanded(
              flex: 1,
              child: Container(
                child: MarketTabs(0),
              )),
          Expanded(
            flex: 9,
            child: Container(
              child:
                  Consumer<ForexDataProvider>(builder: (context, value, child) {
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
    );
  }
}
