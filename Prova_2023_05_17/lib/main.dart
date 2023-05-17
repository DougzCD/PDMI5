import 'dart:js';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Calculadora MMC',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const MyHomePage(title: 'Calculadora MMC'),
    );
  }
}


class MyHomePage extends StatefulWidget {
  const MyHomePage({super.key, required this.title});

  final String title;

  @override
  State<MyHomePage> createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {

  double _resp = 0;
  double n1 = 0;
  double n2 = 0;


  void _MMC(double n1, double n2) {

    double _resto = 0;
    double a = n1;
    double b = n2;

    do{
      _resto = a % b;
      a = b;
      b = _resto;
    }while(_resto != 0);

    setState(() {
      _resp = (( n1 * n2 ) ~/ a) as double;
    });
  }

  @override
  Widget build(BuildContext context) {

    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title),
      ),
      body: Center(
        child: Builder(
          builder: (context) => Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              const Text(
                'Calculadora MMC',
                style: TextStyle(fontSize: 30),
              ),
              SizedBox(height: 20,),


              TextField(
                decoration: InputDecoration(
                  hintText: 'Primeiro Numero',
                ),
                keyboardType: TextInputType.numberWithOptions(decimal: true),
                inputFormatters: <TextInputFormatter>[
                  FilteringTextInputFormatter.allow(RegExp(r'[0-9]+[,.]{0,1}[0-9]*')),
                  TextInputFormatter.withFunction(
                        (oldValue, newValue) => newValue.copyWith(
                      text: newValue.text.replaceAll('.', ','),
                    ),
                  ),
                ],
                onChanged: (newValue) => n1 = double.parse(newValue),
              ),
              TextFormField(

                decoration: InputDecoration(
                  hintText: 'Segundo Numero',
                ),
                keyboardType: TextInputType.numberWithOptions(decimal: true),
                inputFormatters: <TextInputFormatter>[
                  FilteringTextInputFormatter.allow(RegExp(r'[0-9]+[,.]{0,1}[0-9]*')),
                  TextInputFormatter.withFunction(
                        (oldValue, newValue) => newValue.copyWith(
                      text: newValue.text.replaceAll('.', ','),
                    ),
                  ),
                ],
                onChanged: (newValue) => n2 = double.parse(newValue),
              ),
              TextButton(
                style: ButtonStyle(
                  foregroundColor: MaterialStateProperty.all<Color>(Colors.blue),
                ),
                onPressed: () { _MMC(n1, n2);},
                child: Text('Calcular'),
              ),
              Text(
                'Resposta: $_resp!',
                style: TextStyle(fontSize: 30),
              ),

            ],
          ),),
      ),
    );

  }
}
