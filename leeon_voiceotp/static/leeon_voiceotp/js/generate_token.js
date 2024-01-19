// generate_token.js

// (function($) {
//     $(document).ready(function() {
//         $('#id_linktoken').closest('.form-row').hide();  // Ẩn trường linktoken ban đầu

//         // Bắt sự kiện khi ấn nút "Save" hoặc "Save and add another"
//         $('.submit-row input[type="submit"]').on('click', function() {
//             const linktokenField = $('#id_linktoken');
//             if (!linktokenField.val()) {
//                 // Sinh token nếu trường linktoken không có giá trị
//                 const generatedToken = generateToken();
//                 linktokenField.val(generatedToken);
//                 console.log("Generated Token: " + generatedToken);
//             }
//         });
//     });

//     // Hàm sinh token
//     function generateToken() {
//         const length = 64;
//         const charset = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-._~';
//         let token = '';
//         for (let i = 0; i < length; i++) {
//             const randomIndex = Math.floor(Math.random() * charset.length);
//             token += charset[randomIndex];
//         }
//         return token;
//     }
// })(django.jQuery);

// Trong generate_token.js
(function($) {
    $(document).ready(function() {
        $('#id_linktoken').closest('.form-row').hide();  // Ẩn trường linktoken ban đầu

        // Bắt sự kiện khi ấn nút "Save" hoặc "Save and add another"
        $('.submit-row input[type="submit"]').on('click', function() {
            const linktokenField = $('#id_linktoken');
            if (!linktokenField.val()) {
                // Sinh token nếu trường linktoken không có giá trị
                const generatedToken = generateToken();
                linktokenField.val(generatedToken);

                // Gọi API để lưu token
                saveTokenToServer(generatedToken);
            }
        });
    });

    // Hàm gọi API để lưu token
    function saveTokenToServer(token) {
        const otpVendorId = $('#id').val();  // Lấy id của OtpVendor từ trang hiện tại
        const url = `/path/to/save-token/`;  // Điều chỉnh đường dẫn API tùy thuộc vào cấu trúc URL của bạn

        fetch(url, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': getCookie('csrftoken'),  // Cung cấp CSRF token nếu sử dụng Django CSRF protection
            },
            body: JSON.stringify({ otp_vendor_id: otpVendorId }),
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);  // Xử lý kết quả từ server nếu cần
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }

    // Hàm lấy giá trị của cookie theo tên
    function getCookie(name) {
        const value = `; ${document.cookie}`;
        const parts = value.split(`; ${name}=`);
        if (parts.length === 2) return parts.pop().split(';').shift();
    }
})(django.jQuery);

