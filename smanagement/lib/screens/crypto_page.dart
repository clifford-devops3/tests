import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:smanagement/controller/crypto_data.dart';
import 'package:smanagement/controller/forex_data.dart';
import 'package:smanagement/shared/bottom_navigation.dart';
import 'package:smanagement/shared/market_tabs.dart';

class CryptoPage extends StatefulWidget {
  const CryptoPage({Key? key}) : super(key: key);

  @override
  State<CryptoPage> createState() => _CryptoPageState();
}

class _CryptoPageState extends State<CryptoPage> {
  @override
  void initState() {
    // TODO: implement initState
    context.read<CryptoDataProvider>().getCrypto();
    super.initState();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text("Crypto")),
      body: Column(
        children: [
          Expanded(
              flex: 1,
              child: Container(
                child: MarketTabs(1),
              )),
          Expanded(
            flex: 9,
            child: Container(
              child: Consumer<CryptoDataProvider>(
                  builder: (context, value, child) {
                return ListView.builder(
                    itemCount: value.cryptos.length,
                    itemBuilder: (BuildContext context, int index) {
                      return ListTile(
                        leading: Image.network(value.cryptos[index].image!),
                        title: Text(value.cryptos[index].symbol!),
                        subtitle: Text(value.cryptos[index].name!),
                        trailing: Text(
                            value.cryptos[index].current_price!.toString()),
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
