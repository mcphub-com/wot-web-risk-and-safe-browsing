# WOT Web Risk and Safe Browsing MCP Server

## Overview

The WOT Web Risk and Safe Browsing MCP Server provides a comprehensive solution for assessing the reputation and risk profiles of domains or IP addresses. With the power of machine learning algorithms and contributions from a global community of over 140 million users, this server aims to enhance web security, protect users, and enable safe internet exploration.

The server is designed to assess the reputations and risk profiles of various online entities, helping identify potential threats such as phishing, scams, malware, and privacy issues. By utilizing this server, organizations can upgrade their security measures and ensure a safer browsing experience for their users.

## Features

- **Reputation Assessment:** Evaluate the reputation of domains or IP addresses to determine their safety and trustworthiness. The server provides a reputation score on a scale of 0-100, along with a confidence score indicating the reliability of the assessment.

- **Safety Indicators:** Identify potential risks associated with online entities using predefined safety statuses. These statuses provide insights into whether a target is generally safe, not safe, unknown, or suspicious.

- **Child Safety Ratings:** Assess the child safety of domains, ensuring that websites are appropriate and safe for younger audiences.

- **Category Identification:** Discover associated categories for each target, providing additional context and information about the nature of the online entity.

## Usage

### Targets Tool

The Targets Tool is used to request reputations for one or multiple targets. The tool provides detailed insights into the safety and trust levels of specified domains or IP addresses.

- **Functionality:** Retrieve reputation data for up to 10 domains per request.
- **Method:** GET
- **Path:** /targets
- **Query Structure:** Use the parameter `t` to specify target names. This parameter can appear multiple times based on subscription plans.

#### Output

The tool returns an array of results in JSON format, with each result containing:

- **Reputation and Safety Information:** Status, reputation score, and confidence score for both general safety and child safety.
- **Categories:** An array of category identifiers, friendly names, and confidence values.
- **Target Attributes:** Each target object includes a normalized target name and additional attributes for detailed analysis.

### Tool List

- **Get Reputation Data:** Obtain reputation data for specific domains, up to 10 domains per request, using the provided parameters.

This server is a valuable resource for enhancing web security and protecting users from potential online threats. By leveraging advanced technology and community insights, the WOT Web Risk and Safe Browsing MCP Server offers a reliable solution for maintaining a safer web environment.