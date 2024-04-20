# Bank Account Management System

This project implements a simple bank account management system using Python classes. It includes features such as account creation, balance inquiry, deposits, withdrawals, transfers, and interest rewards for specific account types.

## Table of Contents

- [Bank Account Management System](#bank-account-management-system)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Features](#features)
  - [Installation](#installation)
  - [Usage](#usage)
  - [Classes](#classes)
    - [BankAccount](#bankaccount)
    - [InterestRewardAcct](#interestrewardacct)
    - [SavingsAcct](#savingsacct)
  - [Contributing](#contributing)
  - [License](#license)

## Introduction

This Python project aims to provide a basic framework for managing bank accounts. It utilizes object-oriented programming (OOP) concepts to create and manipulate bank account objects with various functionalities.

## Features

- Create bank accounts with initial balances.
- Check account balances.
- Deposit funds into accounts.
- Withdraw funds from accounts, with balance validation.
- Transfer funds between accounts, with balance validation.
- Support for different types of accounts with varying behaviors (e.g., interest rewards, savings accounts).

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/Prosper41/simple-oop-bank.git


## Classes
BankAccount
Manages basic bank account operations such as balance inquiry, deposits, withdrawals, and transfers.
Includes a custom exception (BalanceException) for handling insufficient balance errors.
InterestRewardAcct
Inherits from BankAccount and adds functionality for interest rewards on deposits.
SavingsAcct
Inherits from InterestRewardAcct and includes additional features such as withdrawal fees for savings accounts.