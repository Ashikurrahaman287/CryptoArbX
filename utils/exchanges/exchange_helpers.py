class ExchangeHelpers:
    @staticmethod
    def calculate_transaction_fee(amount, fee_percentage):
        # Calculate transaction fee based on transaction amount and fee percentage
        fee = amount * fee_percentage
        return fee

    @staticmethod
    def format_order_response(response):
        # Format order execution response for readability
        formatted_response = {
            'order_id': response.get('order_id', None),
            'status': response.get('status', None),
            'filled_amount': response.get('filled_amount', None),
            'average_price': response.get('average_price', None)
        }
        return formatted_response

    @staticmethod
    def handle_api_error(error):
        # Handle common API errors and provide informative error messages
        error_message = 'An error occurred while interacting with the exchange API: '
        if 'message' in error:
            error_message += error['message']
        elif 'error' in error:
            error_message += error['error']
        else:
            error_message += str(error)
        return error_message


