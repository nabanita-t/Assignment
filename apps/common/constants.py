# from datetime import time


class ApplicationMessages:
    """Project wise generic response messages"""

    NEW_CUSTOMER_ONBOARDED = None
    COMMISSION_N_EXIST = "Commission Does Not Exist"
    INVALID_REQUEST = "Invalid Request !"
    IMPROPER_REQUEST = "Please fill all the details properly before saving."
    STORE_EMAIL = "Store with same email already exists. Please use different email id."
    BLANK_REQUEST = "Category Name cannot be blank !"
    BANNER_MAX = "Max 10 Banners can be added. Either delete or edit existing Banners !"
    SIZE_BLANK_REQUEST = "Size title cannot be blank !"
    INVENTORY_N = "Inventory does not exist !"
    INVALID_POSTAL_CODE = "Invalid Postal Code Provided!"
    APPOINTMENT_TIME = "Start Time Cannot Be same as End Time !"
    APPOINTMENT_CUSTOMER = "Appointment for same customer at same date and time already exists !"
    ADDRESS_REQUEST = "Please enter the mandatory fields !"
    TIME_DUPLICATE = "You have entered same values in start and end time!"
    INVALID_DATE = "Appointment date missing!"
    STORE_MISSING = "Store field is empty!"
    INVALID_HOLIDAY = "Invalid Holiday List !"
    INVALID_STORE = "Invalid Stores List !"
    INVALID_PRODUCT = "Please select atleast one product !"
    NAME_ICON = "Name or Icon should not be blank"
    PAY_EXIST = "Payment method already exists"
    NAME_PERCENTAGE = "Name or Percentage should not be blank"
    TAX_EXIST = "Tax already exists"
    TAX_SAME = "Same tax cannot be added twice"
    PAYMENT_SAME = "Same payment method cannot be added twice"
    NAME_BLANK = "Description should not be blank"
    FILE_EXCEEDS_SIZE = "File should be less than "
    DELETED = "Data Deleted"
    N_DELETED = "Payment Method cannot be Deleted as it is associated with a Store"
    STORE_N_DELETE = "Store cannot be deleted in active state"
    MATERIAL_CAT_N_DELETE = "Cannot Delete Material Category"
    EMAIL_REGISTERED = "Email Registered"
    INVALID_EMAIL = "Invalid email provided"
    ROLE_BLANK = "Please select a Role"
    ROLE_BLANK_FOR_USER = "Please select a Role for User:{}"
    SAME_STORE_ONE_PLUS = "Same store selected more than once"
    STORE_BLANK = "Store Blank"
    STAFF_EXIST_IN_STORE = "Staff Already exists in {}"
    REFUND_AMT_LT_ZERO = "Refund amount cannot be zero or less"
    REFUND_AMT_GT_PAID = "Refund amount cannot be greater than the Paid amount"

    # USER Login and Signup
    USER_NOT_EXISTS = "User Does Not Exist"
    EMAIL_NOT_EXISTS = "Email Id is Incorrect !"
    USER_N_EMAIL_EXISTS = "User with this Email Does not Exist"
    LOGIN_FAIL = "Login Failed"
    AVAILABILITY_EXISTS = "Either availability already exists or you entered same values in start and end time!"
    USER_ALREADY_EXIST = "User with this email already Exist!"
    USER_ALREADY_EXIST_DESIGNER = "User with this email already Exist as Designer!"
    USER_ALREADY_EXIST_CUSTOMER = "User with this email already Exist as Customer !"
    USER_ALREADY_EXIST_ADMIN = "User with this email already Exist as Super Admin!"
    USER_ALREADY_EXIST_SUPPLIER = "User with this email already Exist as Supplier!"
    USER_ALREADY_EXIST_MANUFACTURER = (
        "User with this email already Exist as Manufacturer!"
    )
    USER_EXIST_AS = "User with this email already Exist as {}!"
    REGISTERED_WITH_OTHER_DES = "Already registered with another designer"
    EMAIL_REGISTERED_WITH_OTHER_DES = "{} registered with another designer"
    ADMIN_PROFILE_N_EXIST = "Admin Profile Does not Exist"
    DUPLICATE_EMAIL = "{} has been entered more than once!"

    EMAIL_NOT_VERIFIED = (
        "Email is Not Verified, Please verify your email and then Login"
    )
    AUTHENTICATION_FAILED = "Incorrect Credentials"
    INVALID_AUTH_TOKEN = "This link is either invalid or got expired."
    PASSWORD_SHOULD_NOT_SAME = "Current Password and New password should not the same"
    PASSWORD_TOO_SHORT = "Minimum password length is 8 characters"
    PASSWORD_TOO_LONG = "Maximum password length is 25 characters"
    PASSWORD_VALIDATION = "Password must at least contain one UpperCase, one LowerCase and a Special Character"
    CURRENT_PASSWORD_INCORRECT = "Current password is incorrect"
    PASSWORD_CHANGED = "Password Changed Successfully"
    USER_AUTH_FAILED = "User Authentication Failed"

    # Shipping
    PRODUCT_CODE_EXISTS = " Product Code Already Exists!"
    HS_CODE_N_EXISTS = " HS Code Does Not Exist!"

    # MAILS
    EMAIL_MISSING = "Please enter the Email"
    RESET_EMAIL_SUBJECT = "Reset Password"
    EMAIL_LIMIT_EXCEED = "Emails limit exceeded, Please try again later"
    REST_PASSWORD_LINK_SENT = "Reset password link send on your registered email"
    LINK_EXPIRE = "Link already been used or expired !"
    ACC_ALREADY_VERIFIED = "Your account is already verified"

    INVALID_SLUG = "URL Does not Exist or got Expired!"
    INVALID_LINK = "URL Does not Exist"
    SUB_ADMIN_INVITE = "Sub Admin Invitation"
    INVALID_ADDRESS = "Invalid Address Provided"

    REQUEST_ACCEPTED = "Congratulations, Your request for designer has been Accepted !"
    REQUEST_REJECTED = "Your request for designer has been Rejected !"
    REQUEST_REJECTED_LOGIN = (
        "Your request for designer has been Rejected, Please Contact Admin"
    )
    REQUEST_PENDING_LOGIN = (
        "Your request for designer is still in Pending, Please Contact Admin"
    )
    ACC_ALREADY_ACTIVE = "Your account already been active"
    NEW_DESIGNER_ALERT = "Designer Notification: New Request Received"
    DESIGNER_INACTIVE = "User has been Blocked by Admin!"
    DESIGNER_ACC_CREATED = "Congratulations!!, your Designer profile has been created"

    PASSWORD_MISSING = "Please enter the Password"

    OTP_SENT_SUCCESSFULLY = "OTP sent successfully"
    TOO_MANY_OTP = "Too many requests, please try again after some time"
    OTP_VERIFIED_SUCCESSFULLY = "OTP Verified Successfully"
    OTP_WRONG = "You entered incorrect OTP"
    PHONE_NUMBER_NOT_VALID = "Phone number is not valid"
    WRONG_EMAIL_PASSWORD = "The password you entered is incorrect. Please try again."

    DATA_NOT_EXIST = "Data Does not Exist!"
    CMS_CREATED = "CMS created"
    CMS_UPDATED = "CMS Updated"

    USER_LOG_OUT = "Logout Successfully!"
    REG_FAILED = "Registration Failed !"
    USER_CREATED = "Account Created Successfully"

    # Customer Messages
    CUSTOMER_EXISTS = "Customer with this email already Exist, please login to continue."
    CUSTOMER_PH_EXISTS = "Customer with this phone number already Exist, please login to continue."
    CUSTOMER_PH_N_EXISTS = "Customer with this phone number does not exist."
    SIGN_UP_2_FAIL = "Customer Signup Step 2 pending"


    # Designer Messages
    BANK_SUCCESS = "Bank Details Successfully added"
    BANK_N_EDIT = "You are Not Allowed To Edit Your Bank Details !"
    BANK_N_EXIST = "Bank Details Does not Exist"
    BANK_STRIPE_N_EXIST = "Bank Details Does not Exist"
    PROFILE_PAGE_2_ERROR = "Please Go Back to Signup page and register the email first!"
    PROFILE_ERROR = "The Profile that you are trying to create is already exist!"
    PROFILE_SUCCESS = "Profile Created Successfully"
    PROFILE_UPDATED = "Profile Updated Successfully"
    DESIGNER_N_EXIST = "Designer Profile Does not exist"
    MANUFACTURER_N_EXIST = "Manufacturer Profile Does not exist"
    DESIGNER_ALREADY_EXIST = "User with this email already exist!"
    DESIGNER_PHONE_ALREADY_EXIST = "User with this Phone number already exist!"
    CUSTOMER_PHONE_ALREADY_EXIST = "User with this Phone number already exist!"
    CATEGORY_NOT_EXISTS = "Category does not exist"
    BANNER_NOT_EXISTS = "Banner does not exist"
    CATEGORY_IN_USE = "Category is in Use"
    UNIT_IN_USE = "Unit is in Use."
    INVALID_CUSTOMER = "The User Already Exist as "
    PERMISSION_DENIED = "Permission Denied"
    STORE_DELETE = "Store cannot be deleted."
    STORE_DELETED = "Store deleted."
    CREDIT_EXPIRE = "Credit Note Expiry Date Set"
    BANK_N_ALLOWED = "You can not delete your default bank account"
    SUCCESS = "Success"
    UPDATE_SUCCESS = "Product Inventory Updated Successfully"
    STOCK_N_NEGATIVE = "Stock cannot be negative"
    PAYMENT_NOT_ALLOWED = "Atleast 1 System Method is Mandatory"
    ONLINE_DATA = "Online Inventory cannot be left null"
    STORE_DATA = "Store Inventory  cannot be left null"
    PRODUCT_N_EXIST = "Product with this barcode does not exist"
    COMMISSION_SUCCESS = "Commission Updated Successfully"
    NOT_SUPPORTED = "Sorry The Application Not Available In This Country"
    MATERIAL_NOT_EXISTS = "Material does not exist"
    VARIANT_NOT_EXISTS = "This Variant does not exist"
    MATERIAL_IN_ORDER_CHECKOUT = "Material exists in an order checkout"
    MATERIAL_IN_CART = "Material exists in a cart"
    MATERIAL_IN_ORDER = "Material exists in an order"

    # POS Messages
    SINGLE_PRIMARY = "Please select only one member as primary!"
    ONE_PRIMARY = "At least one staff member should be primary"
    STAFF_EXIST = "Staff Member Already Exists"
    PRIMARY_N_DEACTIVATED = "Primary member can't be deactivated"
    PRIMARY_N_DELETED = "Primary member can't be deleted"
    DIFFERENT_PIN = "Please enter a different PIN"
    STORE_EDIT_SUCCESS = "Store Details Updated Successfully"
    STAFF_MEMBER_SUCCESS = "New staff member added successfully"
    STAFF_PIN = "Staff Pin not provided"
    WRONG_PIN = "Incorrect Staff Pin provided"
    STAFF_MEMBER_UPDATE = "Staff member data updated successfully"
    STAFF_MEMBER_DELETED = "Staff member deleted successfully"
    PIN_GENERATED = "Pin Generated successfully!"
    USER_AS_OTHER = "User with email:'{}' is already registered as a {}"
    STAFF_DEACTIVATED = "NFX Seller POS Account Deactivated"
    UNAUTHORIZED_ACCESS = "Unauthorized Access"
    CANNOT_DEL_SELF = "Cannot Delete Yourself!"
    POS_ACCOUNT_DISABLED = "Your POS Account has been disabled"
    INACTIVE_N_PRIMARY = "Inactive member cannot be made Primary"
    PRIMARY_NOT_INACTIVE = "Primary member cannot be Inactive"
    DELIVERY_N_LESS_TODAY = "Delivery Date cannot be less than today"
    NAME_N_BLANK = "Name cannot be blank"
    # do not change REMOVE_COUPON_POS message
    REMOVE_COUPON_POS = "Coupon has been used for this Customer, Please remove the coupon or change the customer"

    # Template Message
    TEMPLATE_CREATED = "Template Created"
    TEMPLATE_UPDATED = "Template Updated"
    TEMPLATE_DELETED = "Template Deleted"
    TEMPLATE_ADDED = "Template Added"
    TEMPLATE_NOT_EXIST = "Template Does not Exist"
    PARENT_OPTION_NOT_EXIST = "Parent Option Does not Exist"

    MEASUREMENT_CREATED = "Measurements created"
    MEASUREMENT_UPDATED = "Measurements updated"
    MEASUREMENT_DELETED = "Measurements Deleted"
    MEASUREMENT_N_FOUND = "Measurements not found"
    OPTION_CREATED = "Option created"
    OPTION_UPDATED = "Option updated"
    OPTION_DELETED = "Option Deleted"

    IMAGE_UPLOAD_FAILED = "Image Upload Failed !"
    IMAGE_UPLOAD_SUCCESS = "Image Added Successfully!"
    SKETCH_CREATED = "Sketch Created"
    SKETCH_UPDATED = "Sketch Updated"
    SKETCH_DELETED = "Sketch Deleted Successfully"
    SKETCH_N_EXIST = "Sketch Does Not Exist"
    MATERIAL_CREATED = "Material Created"
    MATERIAL_DELETED = "Material Deleted"
    MATERIAL_N_EXIST = "Material Does Not Exist"
    ACCESSORY_CREATED = "Accessory Created"
    ACCESSORY_DELETED = "Accessory Deleted"
    ACCESSORY_N_EXIST = "Accessory does not exist"
    SIZE_TEMPLATE_N_FOUND = "No Size Template Found"
    SIZE_DELETED = "Size Deleted Successfully"
    SIZE_NOT_EXIST = "Size Does Not Exist"
    SIZE_ALREADY_EXIST = "Size already Exists!"
    CAT_ALREADY_EXIST = "Category already Exists!"
    SUB_CAT_ALREADY_EXIST = "Sub-Category already Exists!"
    UNIT_ALREADY_EXIST = "Unit already Exists!"
    SIZE_INVALID = "Invalid Size Request"
    SIZE_IN_USE = "Size is in use"

    # Product
    PRODUCT_N_EXIST = "Product Does not exist"
    VARIANT_PRODUCT_N_EXIST = "Variant Does Not Exist"
    VARIANT_PRODUCT_EXIST = "Variant Already Exist!"
    PRODUCT_COLOUR_N_EXIST = "Colour Does Not Exist"
    SHIPPING_CREATED = "Shipping Details Added Successfully"
    SHIPPING_N_EXISTS = "Shipping Details Does Not Exist!"
    PRODUCT_UPDATED = "Product Status Updated Successfully !"
    PRODUCT_OPTIONS_UPDATED = "Product Updated Successfully!"
    PRODUCT_ADDED_CART = "Product Added to Cart"
    ANONYM_USER = "Wishlist cannot be added without login/signup"
    SAMPLE_ADDED_CART = "Sample Material Added to Cart"
    CART_PRODUCT_DELETED = "Product Removed from the Cart"
    PRODUCT_DELETED_SUCCESSFULLY = "Product deleted successfully"
    PRODUCT_PRICE_GRT = "Minimum Price Should be $1"
    ZONE_PRICE_GRT = "Zone price cannot be greater than maximum price."
    DESIGNER_N_ALLOWED = "You can not edit template of published product"
    PRODUCT_N_DELETE = "The requested action is not allowed. There are ongoing orders associated with this product."
    VARIANT_N_DELETE = "The requested action is not allowed. There are ongoing orders associated with this variant."

    # publish product
    PRODUCT_PUBLISHED = "Your Product Published Successfully"
    PRODUCT_UN_PUBLISHED = "Your Product UnPublished Successfully"
    PUBLISH_N_VARIANT = "You need to create at least one Variant to Publish the Product"
    PUBLISH_N_SHIPPING = "Please add the shipping details"
    PUBLISH_N_ZONE = "Please add the shipping zones"
    SUB_PUBLISH_N_ZONE = "Please add shipping zone or contact Seller for permission to add shipping zone"
    PUBLISH_N_MEASUREMENT = (
        "You cannot Publish the Product, without selecting any Measurement"
    )
    PUBLISH_N_PRICE = "You cannot Publish the Product, with 0 price"
    PUBLISH_N_OPTIONS = "Please add or select product options"
    PUBLISH_N_INVENTORY = "Please add stock for at least one variant"
    PUBLISH_N_WAREHOUSE = "Please add the ware house address details"
    SUB_PUBLISH_N_WAREHOUSE = "Please add Warehouse address or contact Seller for permission to add Warehouse Details"

    SOMETHING_WENT_WRONG = "Something went wrong"
    CASHBOX_N_DELETED = "Cashbox cannot be deleted since it has sessions attached to it."
    HOLIDAY_EXIST = "Entered data is either Invalid or Duplicate."
    AVAILABILITY_EXIST = "Some of the Availability provided, already exists"
    DATA_N = "All fields are mandatory and Start Time and End Time should not be same"
    DATA_NT = "Please fill the mandatory fields"
    CASHBOX_SESSION_EXISTS = "This Cashbox is already open. Close it first to open again."
    CASHBOX_ALREADY_CLOSE = "This Cashbox is already closed."
    CASHBOX_CLOSED = "This Cashbox is closed. Open it for transaction."
    CASHBOX_REGISTER_OPEN = "This Cashbox has active register. Close it first."
    COMPLETE_PASSWORD_VALIDATION = (
        "Minimum length of password is 8, Maximum length of password is 24 and contain "
        "one Upper Case, one Lower Case and a Special Character and No Spaces"
    )
    PASSWORDS_ARE_NOT_SAME = "Confirm Password and password are not the same"

    SAVED_ADDRESS_DELETE = "Address deleted successfully"
    SAVED_ADDRESS_NOT_EXIST = "Address does not exists"
    WISHLIST_DELETE = "Product removed successfully from wishlist"
    WISHLIST_NOT_EXIST = "Wish list does not exists"
    WISHLIST_EXIST = "Product already exists in your Wishlist"
    USER_IS_NOT_ACTIVE = "You Account has been blocked, Please Contact Admin"
    IN_ACTIVE = "IN_ACTIVE"
    COMPANY_NAME = "Provide the name of your company"
    COMPANY_SIZE = "Provide the size of your company"

    # Customer Payment Method
    CUS_PMT_SUCCESS = "Payment Method Attached Successfully"
    CUS_PMT_INTENT_SUCCESS = "Payment Intent Created Successfully"
    PAYMENT_METHOD_DELETED = "Payment Method Detached Successfully"

    # Stock
    INVENTORY_N_EXIST = "Inventory Not Found"
    INVENTORY_EDITED = "Inventory Added/Updated Successfully"
    STOCK_CREATED = "Variant Stock created successfully"
    STOCK_DELETED = "Variant Stock Deleted Successfully"
    OUT_OF_STOCK = "The Selected Size Is Out Of Stock!"

    # Designer warehouse address
    WAREHOUSE_ADDRESS_DELETED_SUCCESS = "Warehouse Address Deleted Successfully"
    WAREHOUSE_ADDRESS_DOES_NOT_EXIST = "Warehouse Address does not exists"
    WAREHOUSE_ADDRESS_ALREADY_EXIST = "Warehouse Address already exists"

    # Shipping zone messages
    SHIPPING_ZONE_DOES_NOT_EXIST = "Shipping Zone does not exists"
    SHIPPING_ZONE_UPDATED_SUCCESSFULLY = "Shipping Zone Updated Successfully"
    SHIPPING_ZONE_ALREADY_EXIST = "Shipping Zone already exists"
    PROVIDE_VALID_SHIPPING_ZONE_DATA = "Provide Shipping zone data"

    # Order
    CANCEL_ORDER_NOT_ALLOWED = "You are not allowed to cancel this order!"
    CANCEL_ORDER_N_ALLOWED = "This Order Already Cancelled by Designer!"
    INVALID_ORDER = "Invalid Request !"
    ORDER_PLACED = "Your Order Placed Successfully"
    ORDER_REFUNDED = "Your Order Refunded Successfully"
    STORE_CREDIT_ISSUED = "Store Credit issued successfully"
    CUS_COUPON_PUBLISHED = "Discount Coupon Published"
    DES_COUPON_PUBLISHED = "Admin Discount Coupon Published"
    MARKED_COMPLETE = "Order marked as Completed"
    TRACKING_UPDATED = "Order Tracking Updated Successfully"
    DELIVERY_TYPE_UPDATED = "Order Delivery type updated Successfully"
    CUSTOM_INSTALLMENT_PAID = "Installment paid Successfully"

    APPOINTMENT_COMPLETED = "Your Appointment is Complete!"
    APPOINTMENT_CREATED = "Your Appointment is Created"
    FOLLOW_UP_CREATED = "Your Follow up Appointment created!"
    APPOINTMENT_REQUEST = "Appointment Request Received!"
    APPOINTMENT_CANCELLED = "Your Appointment is Cancelled!"
    APPOINTMENT_DECLINED = "Your Appointment is Declined!"
    APPOINTMENT_UPCOMING = "Your Appointment request is Accepted!"
    APPOINTMENT_RESCHEDULED = "Your Appointment is Rescheduled!"

    ORDER_PENDING = "New Order has been received!"
    ORDER_ACCEPTED = "Your order accepted!"
    ORDER_SHIPPED = "Your order has been shipped!"
    MATERIALS_SHIPPED = "Your materials have been shipped!"
    MATERIALS_DELIVERED = "Materials have been delivered!"
    ORDER_REJECTED = "Your order has been rejected by the Designer!"
    FABRIC_SOURCING = "Your order's fabric sourcing is complete!"
    ALTERATIONS = "Your resample order's alterations are complete!"
    RESAMPLE_QC = "Your resample order's quality check are complete!"
    RESAMPLE_SHIP = "Your resample order has been shipped!"
    RESAMPLE_DEL = "Your resample order has been delivered!"
    RESAMPLE_RECEIVE = "Your order's resampling cost has been received!"
    ORDER_DELIVERED = "Your order has been delivered!"
    PATTERN_MAKING = "Your order's pattern making is complete!"
    PRINT_OR_EMBROIDERY = "Your order's print and embroidery is complete!"
    SEWING = "Your order's sewing is complete!"
    QC_CHECK = "Your order's quality check is complete!"
    RECEIVED_PRODUCTION_COST = "Your order's production cost has been received"
    RECEIVED_SAMPLE_COST = "Your order's sampling cost has been received"
    RECEIVED_RE_SAMPLE_COST = "Your order's re-sampling cost has been received"
    RELEASED_S_C = "Sample Cost Released"
    RELEASED_P_C = "Production Cost Released"
    RELEASED_PP_C = "Pre-Production Cost Released"
    RELEASED_RS_C = "Re-Sample Cost Released"
    ORDER_IN_PROGRESS = "Your order is in progress!"
    DESIGNER_CANCELLED_ORDER = "Your order been cancelled by the Designer!"
    DESIGNER_TERMINATE_ORDER = "Your order been terminated by the Designer!"
    DESIGNER_RELEASE_FUNDS = "Your pre-production funds have been received!"
    DESIGNER_RAISE_QUERY = "Claim Raised on Order!"
    ADMIN_REPLY = "Admin Replied To Claim!"
    DESIGNER_REPLY = "Designer Replied To Claim!"
    MANUFACTURER_REPLY = "Manufacturer Replied To Claim!"
    ADMIN_FINAL_REPLY = "Admin's Resolution To Claim!"
    ADMIN_DISPUTE_RESOLVE = "Your order's dispute has been resolved by Admin!"
    MANUFACTURER_CANCELLED_ORDER = "Your order been cancelled by the Manufacturer!"
    CUSTOMER_CANCELLED_ORDER = "Order has been cancelled by the Customer!"
    SUPPLIER_CANCELLED_THE_ORDER = "Your order been cancelled by the Supplier!"
    SUPPLIER_REJECTED_THE_ORDER = "Your order been rejected by the Supplier!"

    # Review
    REVIEW_ADDED_SUCCESSFULLY = "Review added Successfully"
    REVIEW_DOES_NOT_EXIST = "Review does not exists"
    REVIEW_UPDATE_SUCCESSFULLY = "Review Update Successfully"
    REVIEW_REPORTED_SUCCESSFULLY = "Review Reported Successfully"
    REVIEW_LIKED = "Review Liked"
    REVIEW_UPDATED = "Review Updated"
    PROVIDE_VALID_TYPE = "Provide valid type"
    PRODUCTS_MISSING = "Select Products"
    REVIEW_DELETED_SUCCESSFULLY = "Review Deleted Successfully"
    NOT_ABLE_TO_PROVIDE_REVIEW = "Not eligible for review"
    USER_TRYING_TO_REPORT_SELF_REVIEW = "User cannot report self Review"
    ORDER_NOT_DISPUTE = "This order is not under dispute/ has been resolved already"

    # Discount Coupon
    PLEASE_COMPLETE_FORM = "Please, complete this Form"
    COUPON_N_EXIST = "Coupon Does Not Exist"
    COUPON_EXPIRED = "Coupon Expired!"
    COUPON_DELETED = "Coupon Deleted"
    COUPON_PUBLISHED = "Coupon Published Successfully!"
    COUPON_A_EXIST = "Coupon with this Code Already Exist"
    COUPON_A_USED = "Coupon Already Used"
    COUPON_DATE_VALIDATION = "Please Enter a valid Expiry Date"
    NO_PUBLISHED_PRODUCT = "You Don't have any Published Product"
    COUPON_CREATED = "Coupon Created Successfully! "
    COUPON_N_AVAILABLE = "Coupon is currently unavailable"
    COUPON_USAGE_EXCEED = "Coupon Already been Used"
    COUPON_EXHAUSTED = "Sorry, Coupon Exhausted!"
    COUPON_CANT_USE_HERE = "Coupon Can't be used for any of the Product"
    COUPON_STORE_INVALID = "Coupon Can't be used for this Store"
    CART_EMPTY = "Cart is Empty!"
    COUPON_ADD_MORE_PRODUCTS = "Please add some more products to Cart"
    COUPON_APPLIED = "Coupon Applied"
    COUPON_REMOVED = "Coupon Removed from the Cart"
    COUPON_REQUIREMENT_N_FULFILLED = "Coupon Requirement Does not Fulfilled"
    COUPON_N_EDIT = "You Need to Un-publish the coupon, to change the Coupon Code"
    PRODUCT_ALREADY_DELETED = "This product is already deleted from the store"
    PRODUCT_ADDED = "Products successfully added to the store!"
    PRODUCT_SETTLED = "Inventory settled successfully"
    DEAL_N_EXIST = "Deal Does Not Exist"
    DEAL_DELETED = "Deal Deleted"
    DEAL_STATUS_SUCCESS = "Status Changed Successfully!"
    DEAL_CONFLICTING = "A Deal already exists in this time slot"

    # Checkout Session
    SESSION_EXPIRED = "Customer Checkout Session Expired"
    SESSION_DELETED = "Session Deleted Successfully"
    STORE_CHECKOUT_SESSION_N_EXIST = "Checkout Session Does not Exist"

    # Shipping
    ITEM_N_SHIPPABLE = (
        "Some of your cart Items Can not delivered to your shipping address"
    )

    # Sub admin and role module
    ROLE_DOES_NOT_EXISTS = "Role Does Not Exists"
    ROLE_ALREADY_ASSIGNED = (
        "Role is already assigned to sub-admins please unassigned the role then delete"
    )
    POS_ROLE_ALREADY_ASSIGNED = (
        "Role is already assigned to staff members please un-assign the role then delete"
    )
    ROLE_DELETED_SUCCESSFULLY = "Role Deleted Successfully"
    SUB_ADMIN_DELETED_SUCCESSFULLY = "Sub admin deleted successfully"
    SUB_ADMIN_CREATED_SUCCESSFULLY = "Sub admin created successfully"
    SUB_ADMIN_UPDATED_SUCCESSFULLY = "Sub admin updated successfully"
    PLEASE_SELECT_ROLE = "Please select access roles"
    SKIP_INNER_PERMISSIONS = ['SETTINGS', 'ORDER']

    NEW_COUPON_AVAILABLE = "New Coupon is available"
    NEW_DESIGNER_ONBOARDED = "Welcome to NFX Seller App"
    STAFF_PIN_UPDATED = "Store Pin Updated"

    PAYMENT_REFUND = "Order refund has been initiated"
    PRODUCT_ERROR = "Error occurred while fetching the products"
    TRACKING_URL_ADDED = "Tracking URL added"
    BALANCE_N = "Note is mandatory if balance is insufficient"

    # Custom Notifications
    PLEASE_SELECT_DESIGNER = "Please select at-least 1 designer"
    PLEASE_SELECT_CUSTOMER = "Please select at-least 1 customer"
    PLEASE_SELECT_SUPPLIER = "Please select at-least 1 supplier"
    PLEASE_SELECT_MANUFACTURER = "Please select at-least 1 manufacturer"
    PLEASE_SELECT_STORE = "Please select at-least 1 Store"
    SCHEDULE_DATE_MISSING = "Scheduled Date Is Missing"
    INVALID_SCHEDULED_TIME = (
        "Scheduled Date Time Should be Greater than Current Date Time"
    )
    UPDATE_N_ALLOWED = "Update Not allowed on already sent notification"
    INVALID_FILTER_TYPE_PROVIDED = "Invalid Notification Status Provided "
    INVALID_NOT_TYPE_PROVIDED = "Invalid Notification Type Provided "
    NO_ACTIVE_USER_EXIST = "No Active User Present In The System to send Notification"
    INVALID_USER_TYPE_PROVIDED = "Invalid User Type Provided"

    # Supplier Messages

    SUPPLIER_N_EXIST = "Supplier Profile Does not exist"
    SUPPLIER_ALREADY_EXIST = "User with this email already exist!"
    SUPPLIER_PHONE_ALREADY_EXIST = "User with this Phone number already exist!"
    SUPPLIER_INACTIVE = "Supplier is in-active"
    USER_DETAIL_N_ADD = "User Bank Details cannot be added. Check details again."
    NEW_SUPPLIER_ALERT = "Supplier Notification: New Request Received"
    SUPPLIER_REQUEST_ACCEPTED = (
        "Congratulations, Your request for supplier account has been Accepted !"
    )
    SUPPLIER_REQUEST_REJECTED = "Your request for supplier account has been Rejected !"
    SUPPLIER_ACC_CREATED = "Congratulations!!, your Supplier Profile has been created"
    SUPPLIER_STATUS_UPDATED = "Supplier Status Updated Successfully"
    SUPPLIER_PROFILE_UNDER_REVIEW = "Your request for Supplier Account is under review"

    # Manufacturer Constants
    MANUFACTURER_ACC_CREATED = (
        "Congratulations!!, your Manufacturer Profile has been created"
    )
    MANUFACTURER_REQUEST_ACCEPTED = (
        "Congratulations, Your request for manufacturer account has been Accepted !"
    )
    MANUFACTURER_REQUEST_REJECTED = (
        "Your request for manufacturer account has been Rejected !"
    )
    SAMPLE_PROJECT_ADDED = "Sample Project Added Successfully"
    SAMPLE_PROJECT_UPDATED = "Sample Project Updated Successfully"
    MANUFACTURER_STATUS_UPDATED = "Manufacturer Account Status Updated Successfully"
    MANUFACTURER_PROFILE_UNDER_REVIEW = (
        "Your request for Manufacturer Account is under review"
    )

    # Material Category
    MATERIAL_CATEGORY_CREATED = "Material category created successfully"
    MATERIAL_CATEGORY_UPDATED = "Material category updated successfully"
    PARENT_CATEGORY_REQUIRED = "Parent Category ID Required"
    ADD_N_VARIANT = "Please add at-least one variant"
    VARIANT_CREATED = "Material variants added successfully"
    VARIANT_UPDATED = "Material variants updated successfully"

    TASK_N_PERFORM = "This task cannot be performed"
    USER_TYPE_WRONG = "User Type is not valid"
    ACTION_WRONG = "You cannot perform that action"
    INVALID_ACTION = "Invalid shortlist type provided"
    USER_SHORTLIST = "User has been shortlisted successfully"

    ITEM_N_EXIST = "Item does not exist in the cart"

    # Commission
    COMMISSION_GRT_ZERO = "Commission must be greater than zero"

    # Quotation
    QUOTATION_OPTIONS_UPDATED = "Quotation Updated Successfully!"

    # Capabilities
    CAPABILITY_IN_USE = "Capability is in use"
    GC_IN_USE = "Garment Category is in use"

    # Designer Cart
    CART_ITEM_EXISTS = "This Item already exists in the cart"

    # Manufacturer Offers
    PRODUCTION_COST_CREATED = "Production Cost added successfully"
    SAMPLING_COST_CREATED = "Sampling Cost added successfully"
    MATERIAL_COST_CREATED = "Material Cost added successfully"

    # Chat
    BLOCKED = "You have successfully blocked the user"
    UN_BLOCKED = "You have successfully un-blocked the user"
    OFFER_STATUS_CHANGED = "Offer Status Updated Successfully"

    # MF-DF Orders
    STATUS_UPDATED = "Status Updated"
    INVALID_DATA_PROVIDED = "Invalid Data Provided"
    Q_SAVED_AS_DRAFT = "Quotation Saved As Draft"
    Q_SHARED_SUCCESSFULLY = "Quotation shared successfully"
    SAMPLING_DATA_UNAVAILABLE = "Sampling Cost Details Un-Available"

    PAYMENT_CREATED = "Payment Method Created"
    PAYMENT_EDITED = "Payment Method updated Successfully"
    APPOINTMENT_STATUS = "Appointment status updated successfully"
    TAX_EDITED = "Tax Data updated Successfully"
    CASH_BOX_EDITED = "Cashbox Data updated Successfully"


class Constant:
    """Constants Values"""

    PUBLISHED = "PUBLISHED"
    DEFAULT_SIZE_ID = "39fea36c-6099-4de2-a2ac-b059ba90276f"
    DRAFT = "DRAFT"
    CLOSED = "CLOSED"
    LAUNCHED = "LAUNCHED"
    POS_REVENUE = "POS_REVENUE"
    POS_REVENUE_ADMIN = "POS_REVENUE_ADMIN"
    POS_ORDERS = "POS_ORDERS"
    POS_REFUNDS = "POS_REFUNDS"

    COMPLETED = "COMPLETED"
    CANCELLED = "CANCELLED"
    APPOINTMENT_CANCELLED = "APPOINTMENT_CANCELLED"
    APPOINTMENT_CREATED = "APPOINTMENT_CREATED"
    FOLLOW_UP = "FOLLOW_UP"
    CUS_FOLLOW_UP = "CUS_FOLLOW_UP"
    APPOINTMENT_REQ = "APPOINTMENT_REQUESTED"
    DECLINED = "DECLINED"
    UPCOMING = "UPCOMING"
    RESCHEDULED = "RESCHEDULED"
    SCHEDULE_FOLLOW_UP = "SCHEDULE_FOLLOW_UP"

    MONDAY = "MONDAY"
    TUESDAY = "TUESDAY"
    WEDNESDAY = "WEDNESDAY"
    THURSDAY = "THURSDAY"
    FRIDAY = "FRIDAY"
    SATURDAY = "SATURDAY"
    SUNDAY = "SUNDAY"

    SALE = "SALE"
    REFUND = "REFUND"
    PARTIAL_REFUND = "PARTIAL_REFUND"
    PARTIAL_PAYMENT = "PARTIAL_PAYMENT"
    PETTY_CASH = "PETTY_CASH"

    CASH_IN = "CASH_IN"
    CASH_OUT = "CASH_OUT"

    EMAIL_LINK_EXPIRY = 8  # Hours
    DATA_UPLOAD_MAX_MEMORY_SIZE = 100000000  # 100 MB
    EMAIL_ELIGIBILITY_HOURS = 2  # HOURS
    MINIMUM_STOCK_LIMIT = 10

    SUCCESS = "Success"
    DATA_SAVED = "Data Saved"
    ERROR_OCCURRED = "Some Error Occurred"
    BAD_REQUEST = "BAD REQUEST!"
    FIELDS_MISSING = "Data Invalid.Check the provided data again."
    DATA_DELETED = "Deleted"
    PAYMENT_DELETED = "Payment Method Deleted"
    STORE_DELETED = "Store Deleted"
    TAX_DELETED = "Tax Deleted"
    CASH_BOX_DELETED = "Cashbox Deleted"
    CASHBOX_REGISTER_NOT_OPEN = "There are no open registers for this cashbox, kindly reload the cashbox list"
    AVAILABILITY_DELETED = "Availability Deleted"
    HOLIDAY_DELETED = "Holiday Deleted"
    DATA_N_EXIST = "Data Does not exits"

    CUSTOMER = "Customers"
    DESIGNER = "Fashion Designers"
    MANUFACTURERS = "Manufacturers"
    SUPPLIERS = "Suppliers"

    # SLUGS
    PROFILE_SLUG = "PROFILE_URL_SLUG"
    FORGET_PASSWORD_SLUG = "FORGET_PASSWORD_SLUG"
    EMAIL_VERIFICATION_SLUG = "EMAIL_VERIFICATION_SLUG"

    # permission name, Please DO NOT CHANGE
    CUSTOMER_PERMISSION_NAME = "CUSTOMER"
    DESIGNER_PERMISSION_NAME = "DESIGNER"
    SUPER_ADMIN_PERMISSION_NAME = "SUPER_ADMIN"
    MANUFACTURER = "MANUFACTURER"
    SUPPLIER = "SUPPLIER"
    BOTH = "BOTH"
    POS_USER = "POS_USER"
    POS_REVENUE_REPORTS = "POS_REVENUE_REPORTS"
    AD_FD_REVENUE_REPORTS = "REVENUE_REPORTS"
    AD_REVENUE_REPORTS = "ADMIN_REVENUE_REPORTS"
    POS_REFUND_REPORTS = "POS_REFUND_REPORTS"
    AD_FD_REFUND_REPORTS = "REFUND_REPORTS"
    POS_ORDER_REPORTS = "POS_ORDER_REPORTS"
    AD_FD_ORDER_REPORTS = "ORDER_REPORTS"
    POS_PRODUCT_REPORTS = "POS_PRODUCT_REPORTS"
    POS_STAFF_REPORTS = "POS_STAFF_REPORTS"
    AD_FD_STAFF_REPORTS = "STAFF_REPORTS"
    POS_TRANSACTION_REPORTS = "POS_TRANSACTION_REPORTS"
    AD_FD_TRANSACTION_REPORTS = "TRANSACTION_REPORTS"
    POS_INVENTORY_REPORTS = "POS_INVENTORY_REPORTS"
    AD_FD_INVENTORY_REPORTS = "INVENTORY_REPORTS"
    AD_FD_CUSTOMER_REPORTS = "CUSTOMER_REPORTS"
    AD_FD_STORE_REPORTS = "STORE_REPORTS"
    AD_FD_CREDIT_REPORTS = "CREDIT_REPORTS"
    POS_CASHBOX_REPORTS = "POS_CASHBOX_REPORTS"

    APPROVED = "APPROVED"
    ACCEPTED = "ACCEPTED"
    CREATED = "CREATED"
    PENDING = "PENDING"
    REJECTED = "REJECTED"
    USER_INACTIVE = "USER_INACTIVE"

    # Gender
    MALE = "MALE"
    FEMALE = "FEMALE"
    OTHERS = "OTHERS"

    INVALID_CONTENT_TYPE = "Invalid Component Type"

    APPROVE = "APPROVE"
    REJECT = "REJECT"

    FAILED = "FAILED"
    SUCCESSFUL = "SUCCESS"

    WEB = "WEB"
    ANDROID = "MOBILE"
    IOS = "IOS"

    YEARLY = "YEARLY"
    MONTHLY = "MONTHLY"
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"


class OnBoardingMessages(object):
    USER_REG_SUCCESS = "User Registration Successful"
    EMAIL_REG_FAILED = "Email Registration Failed, User Already Exists"
    LOGIN_SUCCESS = "Login success"
    LOGIN_FAILED = "Login failed"
    USER_DOES_NOT_EXISTS = "User with this Email doesn't Exist"
    INVALID_PHONE = "Invalid Phone Number"
    INCORRECT_PASSWORD = "Wrong Password"
    PHONE_NUMBER_UPDATED_SUCCESSFULLY = "Phone Number Registered Successfully"
    MOBILE_REG_FAILED = "Mobile Registration Failed"
    MOBILE_LOGIN_USER_NOT_EXISTS = "Phone number is not registered with us"
    MOBILE_REGISTER_SUCCESS = "Mobile Registration Successful"
    OTP_SENT_SUCCESS = "We have sent a 6-digit verification code to you"
    OTP_SENT_FAIL = "There was an error in sending OTP, Please try again later"
    OTP_VALIDATE_SUCCESS = "Your number has been verified successfully"
    OTP_VALIDATE_FAIL = "The OTP Entered Is Incorrect!"
    OTP_LIMIT_REACHED = (
        "You Have Reached Maximum of 5 OTP Attempts Please Try Again After 30 Minutes"
    )
    INVALID_POSTAL_CODE = "Invalid Postal Code Provided!"
    INVALID_COUNTRY_VS_PHONE = "Invalid Country or Phone Number Provided!"
    DESIGNER_N_BRAND = "Designer without brand name cannot be accepted!"


messages = OnBoardingMessages()


class FetchErrorMessages:
    def __init__(self, table_name):
        self.table_name = table_name

    def get_error_message(self):
        # customer app
        if self.table_name == "CustomerProfile":
            return messages.USER_DOES_NOT_EXISTS
        elif self.table_name == "SavedAddress":
            return ApplicationMessages.SAVED_ADDRESS_NOT_EXIST
        elif self.table_name == "WishList":
            return ApplicationMessages.WISHLIST_NOT_EXIST
        elif self.table_name == "ShoppingCart":
            return ApplicationMessages.ITEM_N_EXIST

        # custom_wear app
        elif self.table_name == "ImportMeasurement":
            return ApplicationMessages.MEASUREMENT_N_FOUND

        # designer app
        elif self.table_name == "DesignerCompany":
            return Constant.COMPANY_DOES_NOW_EXIST
        elif self.table_name == "DressTemplate":
            return ApplicationMessages.TEMPLATE_NOT_EXIST
        elif self.table_name == "SketchesTemplate":
            return ApplicationMessages.TEMPLATE_NOT_EXIST
        elif self.table_name == "WareHouseAddress":
            return ApplicationMessages.WAREHOUSE_ADDRESS_DOES_NOT_EXIST
        elif self.table_name == "DesignerSavedAddress":
            return ApplicationMessages.SAVED_ADDRESS_NOT_EXIST
        elif self.table_name == "DesignerShoppingCart":
            return ApplicationMessages.ITEM_N_EXIST
        elif self.table_name == "DesignerOrder":
            return ApplicationMessages.INVALID_ORDER
        elif self.table_name == "DesignerOrderDetail":
            return ApplicationMessages.INVALID_ORDER
        elif self.table_name == "DesignerOrderItem":
            return ApplicationMessages.INVALID_ORDER

        # discount app
        elif self.table_name == "DiscountCoupon":
            return ApplicationMessages.COUPON_N_EXIST
        elif self.table_name == "Deal":
            return ApplicationMessages.DEAL_N_EXIST

        # inventory app
        elif self.table_name == "Inventory":
            return ApplicationMessages.INVENTORY_N_EXIST

        # manufacturer app
        elif self.table_name == "ManufacturerWareHouseAddress":
            return ApplicationMessages.WAREHOUSE_ADDRESS_DOES_NOT_EXIST

        # payment app
        elif self.table_name == "DesignerStripeDetail":
            return stripe_constants.DESIGNER_STRIPE_N_EXIST
        elif self.table_name == "DesignerBankDetails":
            return ApplicationMessages.BANK_STRIPE_N_EXIST
        elif self.table_name == "UserStripeDetail":
            return stripe_constants.USER_STRIPE_N_EXIST
        elif self.table_name == "UserBankDetails":
            return ApplicationMessages.BANK_STRIPE_N_EXIST

        # product app
        elif self.table_name == "Category":
            return ApplicationMessages.CATEGORY_NOT_EXISTS
        elif self.table_name == "Size":
            return ApplicationMessages.SIZE_NOT_EXIST
        elif self.table_name == "SizeTemplate":
            return ApplicationMessages.CATEGORY_NOT_EXISTS
        elif self.table_name == "DesignerProduct":
            return ApplicationMessages.PRODUCT_N_EXIST
        elif self.table_name == "ShippingProduct":
            return ApplicationMessages.SHIPPING_N_EXISTS

        # super_admin app
        elif self.table_name == "SuperAdminProfile":
            return ApplicationMessages.ADMIN_PROFILE_N_EXIST

        # supplier app
        elif self.table_name == "SupplierWareHouseAddress":
            return ApplicationMessages.WAREHOUSE_ADDRESS_DOES_NOT_EXIST
        elif self.table_name == "MaterialCategory":
            return ApplicationMessages.CATEGORY_NOT_EXISTS
        elif self.table_name == "Material":
            return ApplicationMessages.MATERIAL_NOT_EXISTS
        elif self.table_name == "MaterialVariant":
            return ApplicationMessages.VARIANT_NOT_EXISTS
        elif self.table_name == "ShippingMaterial":
            return ApplicationMessages.SHIPPING_N_EXISTS
        elif self.table_name == "StoreCheckoutSession":
            return ApplicationMessages.STORE_CHECKOUT_SESSION_N_EXIST
        else:
            return Constant.BAD_REQUEST
