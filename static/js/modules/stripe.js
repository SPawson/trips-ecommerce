

$(function() {
    Stripe.setPublishableKey('pk_test_TBvGn5FZuepmOCahJChBayZ0005bGN5Vjm')

    $(document).on('submit','#payment-form',function(event) {
        event.preventDefault();
        var form = this;
        var actionEndpoint = $(form).attr('action')
        var card = {
            number: $("#id_credit_card_number").val(),
            expMonth: $("#id_expiry_month").val(),
            expYear: $("#id_expiry_year").val(),
            cvc: $("#id_cvv").val()
        };

        Stripe.createToken(card, function(status, response) {
            if (status ==200){
                $("#credit-card-errors").hide();
                $("#id_stripe_id").val(response.id);  

                $("#id_credit_card_number").removeAttr('name');
                $("#id_cvv").removeAttr('name');
                $('#id_expiry_month').removeAttr('name');
                $('#id_expiry_year').removeAttr('name');

                $.ajax({
                    type:'POST',
                    url: actionEndpoint,
                    data: $(form).serialize(),
                    success:function(data){
                        swal({
                            title: "Payment Successful!",
                            text: "We hope you enjoy your trip",
                            icon: "success",
                            button: "Thanks!",
                          }).then(() => {
                            window.location=data.url;
                          });;
                    },
                    error: function(data){
                        let message ='The billing form contains errors';
                        let title = 'Form Error';
                        let response = data.responseJSON;
                        let errors;
                        console.log(data.responseText);
                        console.log(data.responseJSON);

                        //TODO:
                        //Render django forms validation messages

                        // for (i=0; i > response.length; i++){
                        //     errors
                        // };

                        if (data.stripe == 'error'){
                            title = 'Error Encountered'
                            message = "Stripe encountered an issue, please try again later"
                        }
   
                        console.log(data)
                        swal({
                            title: title,
                            text: message,
                            icon: "error",
                            button: "Ok",
                          });
                    }
                })
            }
            else {
                // $("#stripe-error-message").text(response.error.message);
                // $("#credit-card-errors").show();
                // $("#validate_card_btn").attr("disabled", false);
                swal({
                    title: "Card Error",
                    text: response.error.message,
                    icon: "error",
                    button: "Ok",
                  });
            }
        });
        return false;
    });
})

